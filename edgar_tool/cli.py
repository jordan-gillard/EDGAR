import time
from datetime import date, datetime
from typing import Optional

import typer
from thefuzz import fuzz, process
from typing_extensions import Annotated

from .location_autocomplete import LOCATION_CODE_TO_NAME

from .constants import DateRange, Filing, FilingCategory, Location
from .rss import fetch_rss_feed
from .text_search import EdgarTextSearcher, SearchParams

app = typer.Typer(name="edgar", no_args_is_help=True)


def text_search_output_callback(value: str):
    if not value.endswith(("csv", "json", "jsonl")):
        raise typer.BadParameter(
            f"Unsupported file extension for destination file: {value} "
            "(should be one of csv, json, or jsonl)."
        )
    return value


def location_help_callback(incomplete: str):
    """
    Provides fuzzy-matched location suggestions for the user's CLI (tab completion).
    """
    location_lookup = {}
    # TODO: What if we used two different fuzzy matching algorithms?
    #  One for names and one for codes? Then we could keep the highest scorers from each.
    for code, name in LOCATION_CODE_TO_NAME:
        # Use both code and name as keys for fuzzy matching, since the user can input either.
        location_lookup[code] = (code, name)
        location_lookup[name] = (code, name)

    fuzzy_results = process.extract(
        incomplete,
        list(location_lookup.keys()),
        limit=20,
    )

    # This threshold was determined after a lot of trial and error.
    # If it's too low, we'll get too many strings that don't make sense for the user's input.
    # If it's too high then it doesn't tolerate typos well.
    # 81 seems perfect for tolerating a small typo while still being accurate.
    threshold = 80
    close_matches = (
        match_str for match_str, score in fuzzy_results if score >= threshold
    )

    seen = set()
    for match_str in close_matches:
        pair = location_lookup[match_str]
        if pair not in seen:
            seen.add(pair)
            yield pair


@app.command(
    help=(
        "Perform a custom text search on the SEC EDGAR website and save the results "
        "to either a CSV, JSON, or JSONLines file."
    ),
)
def text_search(
    text: Annotated[
        list[str],
        typer.Argument(
            help=(
                "Search filings for a word or a list of words. "
                "A filing must contain all the words to return. "
                "To search for an exact phrase, use double quotes, like "
                '"fiduciary product".'
            ),
        ),
    ],
    output: Annotated[
        str,
        typer.Option(
            "--output",
            "-o",
            help="Name of the output file to save results to. Accepts .csv, .json, and .jsonl extensions.",
            default_factory=f"edgar_search_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            callback=text_search_output_callback,
        ),
    ],
    date_range: Annotated[
        DateRange,
        typer.Option(
            "--date-range",
            help="Date range of the search. Use 'all' to search all records since 2001.",
        ),
    ] = DateRange.five_years,
    start_date: Annotated[
        datetime,
        typer.Option(
            formats=["%Y-%m-%d"],
            help="Start date of the search in YYYY-MM-DD format (i.e. 2024-07-28). ",
        ),
    ] = None,
    end_date: Annotated[
        datetime,
        typer.Option(
            formats=["%Y-%m-%d"],
            help="End date of the search in YYYY-MM-DD format (i.e. 2024-07-28)",
        ),
    ] = date.today().strftime("%Y-%m-%d"),
    entity_id: Annotated[
        str,
        typer.Option(
            help="Company name, ticker, CIK number or individual's name.",
        ),
    ] = None,
    filing_category: Annotated[
        FilingCategory,
        typer.Option(
            help=(
                "Form group to search for. Use 'custom' or do not set if using "
                "--single-form/-sf."
            ),
        ),
    ] = None,
    single_form: Annotated[
        list[Filing],
        typer.Option(
            "--single-form",
            "-sf",
            help='List of single forms to search for (e.g. `-sf 10-K -sf "PRE 14A")',
        ),
    ] = None,
    peo_in: Annotated[
        Location,
        typer.Option(
            "--principal-executive-offices-in",
            "-peoi",
            help=(
                "Search for the primary location associated with a filing. "
                "The principal executive office is where the company's top "
                "management operates and conducts key business decisions. "
                "The location could be a US state or territory, a Canadian "
                "province, or a country."
            ),
            autocompletion=location_help_callback,
        ),
    ] = None,
    inc_in: Annotated[
        Location,
        typer.Option(
            "--incorporated-in",
            "-ii",
            help=(
                "Search for the primary location associated with a filing. "
                "Incorporated in refers to the location where the company was "
                "legally formed and registered as a corporation. "
                "The location could be a US state or territory, a Canadian "
                "province, or a country."
            ),
            autocompletion=location_help_callback,
        ),
    ] = None,
):
    if start_date and end_date and start_date > end_date:
        raise typer.BadParameter("Start date cannot be later than end date.")

    search_params = SearchParams(
        keywords=text,
        entity=entity_id,
        filing_category=filing_category,
        single_forms=single_form,
        date_range_select=date_range,
        start_date=start_date,
        end_date=end_date,
        peo_in=peo_in,
        inc_in=inc_in,
    )

    text_searcher = EdgarTextSearcher()
    text_searcher.search(
        search_params=search_params,
        destination=output,
    )


def rss_output_callback(value: str):
    if not value.endswith("csv"):
        raise typer.BadParameter(
            f"Unsupported file extension for destination file: {value}. "
            "Only CSV files are supported for RSS feed. Please use a file "
            "that ends with .csv (e.g. --output my_rss_feed.csv)."
        )
    return value


@app.command(
    help=(
        "Fetch the latest RSS feed data for the given company tickers and save it to "
        "either a CSV, JSON, or JSONLines file."
    ),
)
def rss(
    tickers: Annotated[
        list[str],
        typer.Argument(
            help="List of company tickers to fetch the RSS feed for",
        ),
    ],
    output: Annotated[
        str,
        typer.Option(
            "--output",
            "-o",
            help="Name of the output file to save the results to",
            callback=rss_output_callback,
        ),
    ] = f"edgar_rss_feed_{datetime.now().strftime('%d%m%Y_%H%M%S')}.csv",
    refresh_tickers_mapping: Annotated[
        bool,
        typer.Option(
            "--refresh-tickers-mapping",
            "-rtm",
            help="Whether to refresh the company tickers mapping file or not",
        ),
    ] = False,
    every_n_mins: Annotated[
        Optional[int],
        typer.Option(
            "--every-n-mins",
            help="If set, fetch the RSS feed every n minutes",
        ),
    ] = None,
) -> None:
    if every_n_mins:
        while True:
            fetch_rss_feed(tickers, output, refresh_tickers_mapping)
            print(
                f"Sleeping for {every_n_mins} minute(s) before fetching the RSS feed again ..."
            )
            time.sleep(every_n_mins * 60)
    fetch_rss_feed(tickers, output, refresh_tickers_mapping)
