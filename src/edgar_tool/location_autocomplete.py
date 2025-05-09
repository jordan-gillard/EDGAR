from typing import NamedTuple


class LocationCodeAndName(NamedTuple):
    code: str
    name: str


LOCATION_CODE_TO_NAME = [
    LocationCodeAndName("AL", "Alabama"),
    LocationCodeAndName("AK", "Alaska"),
    LocationCodeAndName("AZ", "Arizona"),
    LocationCodeAndName("AR", "Arkansas"),
    LocationCodeAndName("CA", "California"),
    LocationCodeAndName("CO", "Colorado"),
    LocationCodeAndName("CT", "Connecticut"),
    LocationCodeAndName("DE", "Delaware"),
    LocationCodeAndName("DC", "District of Columbia"),
    LocationCodeAndName("FL", "Florida"),
    LocationCodeAndName("GA", "Georgia"),
    LocationCodeAndName("HI", "Hawaii"),
    LocationCodeAndName("ID", "Idaho"),
    LocationCodeAndName("IL", "Illinois"),
    LocationCodeAndName("IN", "Indiana"),
    LocationCodeAndName("IA", "Iowa"),
    LocationCodeAndName("KS", "Kansas"),
    LocationCodeAndName("KY", "Kentucky"),
    LocationCodeAndName("LA", "Louisiana"),
    LocationCodeAndName("ME", "Maine"),
    LocationCodeAndName("MD", "Maryland"),
    LocationCodeAndName("MA", "Massachusetts"),
    LocationCodeAndName("MI", "Michigan"),
    LocationCodeAndName("MN", "Minnesota"),
    LocationCodeAndName("MS", "Mississippi"),
    LocationCodeAndName("MO", "Missouri"),
    LocationCodeAndName("MT", "Montana"),
    LocationCodeAndName("NE", "Nebraska"),
    LocationCodeAndName("NV", "Nevada"),
    LocationCodeAndName("NH", "New Hampshire"),
    LocationCodeAndName("NJ", "New Jersey"),
    LocationCodeAndName("NM", "New Mexico"),
    LocationCodeAndName("NY", "New York"),
    LocationCodeAndName("NC", "North Carolina"),
    LocationCodeAndName("ND", "North Dakota"),
    LocationCodeAndName("OH", "Ohio"),
    LocationCodeAndName("OK", "Oklahoma"),
    LocationCodeAndName("OR", "Oregon"),
    LocationCodeAndName("PA", "Pennsylvania"),
    LocationCodeAndName("RI", "Rhode Island"),
    LocationCodeAndName("SC", "South Carolina"),
    LocationCodeAndName("SD", "South Dakota"),
    LocationCodeAndName("TN", "Tennessee"),
    LocationCodeAndName("TX", "Texas"),
    LocationCodeAndName("UT", "Utah"),
    LocationCodeAndName("VT", "Vermont"),
    LocationCodeAndName("VA", "Virginia"),
    LocationCodeAndName("WA", "Washington"),
    LocationCodeAndName("WV", "West Virginia"),
    LocationCodeAndName("WI", "Wisconsin"),
    LocationCodeAndName("WY", "Wyoming"),
    LocationCodeAndName("AB", "Alberta"),
    LocationCodeAndName("BC", "British Columbia"),
    LocationCodeAndName("CAN", "Canada"),
    LocationCodeAndName("MB", "Manitoba"),
    LocationCodeAndName("NB", "New Brunswick"),
    LocationCodeAndName("NL", "Newfoundland and Labrador"),
    LocationCodeAndName("NS", "Nova Scotia"),
    LocationCodeAndName("ON", "Ontario"),
    LocationCodeAndName("PE", "Prince Edward Island"),
    LocationCodeAndName("QC", "Quebec"),
    LocationCodeAndName("SK", "Saskatchewan"),
    LocationCodeAndName("YT", "Yukon"),
    LocationCodeAndName("AFG", "Afghanistan"),
    LocationCodeAndName("ALA", "Åland Islands"),
    LocationCodeAndName("ALB", "Albania"),
    LocationCodeAndName("DZA", "Algeria"),
    LocationCodeAndName("ASM", "American Samoa"),
    LocationCodeAndName("AND", "Andorra"),
    LocationCodeAndName("AGO", "Angola"),
    LocationCodeAndName("AIA", "Anguilla"),
    LocationCodeAndName("ATA", "Antarctica"),
    LocationCodeAndName("ATG", "Antigua and Barbuda"),
    LocationCodeAndName("ARG", "Argentina"),
    LocationCodeAndName("ARM", "Armenia"),
    LocationCodeAndName("ABW", "Aruba"),
    LocationCodeAndName("AUS", "Australia"),
    LocationCodeAndName("AUT", "Austria"),
    LocationCodeAndName("AZE", "Azerbaijan"),
    LocationCodeAndName("BHS", "Bahamas"),
    LocationCodeAndName("BHR", "Bahrain"),
    LocationCodeAndName("BGD", "Bangladesh"),
    LocationCodeAndName("BRB", "Barbados"),
    LocationCodeAndName("BLR", "Belarus"),
    LocationCodeAndName("BEL", "Belgium"),
    LocationCodeAndName("BLZ", "Belize"),
    LocationCodeAndName("BEN", "Benin"),
    LocationCodeAndName("BMU", "Bermuda"),
    LocationCodeAndName("BTN", "Bhutan"),
    LocationCodeAndName("BOL", "Bolivia, Plurinational State of"),
    LocationCodeAndName("BIH", "Bosnia and Herzegovina"),
    LocationCodeAndName("BWA", "Botswana"),
    LocationCodeAndName("BVT", "Bouvet Island"),
    LocationCodeAndName("BRA", "Brazil"),
    LocationCodeAndName("IOT", "British Indian Ocean Territory"),
    LocationCodeAndName("BRN", "Brunei Darussalam"),
    LocationCodeAndName("BGR", "Bulgaria"),
    LocationCodeAndName("BFA", "Burkina Faso"),
    LocationCodeAndName("BDI", "Burundi"),
    LocationCodeAndName("KHM", "Cambodia"),
    LocationCodeAndName("CMR", "Cameroon"),
    LocationCodeAndName("CPV", "Cabo Verde"),
    LocationCodeAndName("CYM", "Cayman Islands"),
    LocationCodeAndName("CAF", "Central African Republic"),
    LocationCodeAndName("TCD", "Chad"),
    LocationCodeAndName("CHL", "Chile"),
    LocationCodeAndName("CHN", "China"),
    LocationCodeAndName("CXR", "Christmas Island"),
    LocationCodeAndName("CCK", "Cocos (Keeling) Islands"),
    LocationCodeAndName("COL", "Colombia"),
    LocationCodeAndName("COM", "Comoros"),
    LocationCodeAndName("COG", "Republic of the Congo"),
    LocationCodeAndName("COD", "Congo, The Democratic Republic of the"),
    LocationCodeAndName("COK", "Cook Islands"),
    LocationCodeAndName("CRI", "Costa Rica"),
    LocationCodeAndName("CIV", "Côte d'Ivoire"),
    LocationCodeAndName("HRV", "Croatia"),
    LocationCodeAndName("CUB", "Cuba"),
    LocationCodeAndName("CYP", "Cyprus"),
    LocationCodeAndName("CZE", "Czechia"),
    LocationCodeAndName("DNK", "Denmark"),
    LocationCodeAndName("DJI", "Djibouti"),
    LocationCodeAndName("DMA", "Dominica"),
    LocationCodeAndName("DOM", "Dominican Republic"),
    LocationCodeAndName("ECU", "Ecuador"),
    LocationCodeAndName("EGY", "Egypt"),
    LocationCodeAndName("SLV", "El Salvador"),
    LocationCodeAndName("GNQ", "Equatorial Guinea"),
    LocationCodeAndName("ERI", "Eritrea"),
    LocationCodeAndName("EST", "Estonia"),
    LocationCodeAndName("ETH", "Ethiopia"),
    LocationCodeAndName("FLK", "Falkland Islands (Malvinas)"),
    LocationCodeAndName("FRO", "Faroe Islands"),
    LocationCodeAndName("FJI", "Fiji"),
    LocationCodeAndName("FIN", "Finland"),
    LocationCodeAndName("FRA", "France"),
    LocationCodeAndName("GUF", "French Guiana"),
    LocationCodeAndName("PYF", "French Polynesia"),
    LocationCodeAndName("ATF", "French Southern Territories"),
    LocationCodeAndName("GAB", "Gabon"),
    LocationCodeAndName("GMB", "Gambia"),
    LocationCodeAndName("GEO", "Georgia"),
    LocationCodeAndName("DEU", "Germany"),
    LocationCodeAndName("GHA", "Ghana"),
    LocationCodeAndName("GIB", "Gibraltar"),
    LocationCodeAndName("GRC", "Greece"),
    LocationCodeAndName("GRL", "Greenland"),
    LocationCodeAndName("GRD", "Grenada"),
    LocationCodeAndName("GLP", "Guadeloupe"),
    LocationCodeAndName("GUM", "Guam"),
    LocationCodeAndName("GTM", "Guatemala"),
    LocationCodeAndName("GGY", "Guernsey"),
    LocationCodeAndName("GIN", "Guinea"),
    LocationCodeAndName("GNB", "Guinea-Bissau"),
    LocationCodeAndName("GUY", "Guyana"),
    LocationCodeAndName("HTI", "Haiti"),
    LocationCodeAndName("HMD", "Heard Island and McDonald Islands"),
    LocationCodeAndName("VAT", "Holy See (Vatican City State)"),
    LocationCodeAndName("HND", "Honduras"),
    LocationCodeAndName("HKG", "Hong Kong"),
    LocationCodeAndName("HUN", "Hungary"),
    LocationCodeAndName("ISL", "Iceland"),
    LocationCodeAndName("IND", "India"),
    LocationCodeAndName("IDN", "Indonesia"),
    LocationCodeAndName("IRN", "Iran, Islamic Republic of"),
    LocationCodeAndName("IRQ", "Iraq"),
    LocationCodeAndName("IRL", "Ireland"),
    LocationCodeAndName("IMN", "Isle of Man"),
    LocationCodeAndName("ISR", "Israel"),
    LocationCodeAndName("ITA", "Italy"),
    LocationCodeAndName("JAM", "Jamaica"),
    LocationCodeAndName("JPN", "Japan"),
    LocationCodeAndName("JEY", "Jersey"),
    LocationCodeAndName("JOR", "Jordan"),
    LocationCodeAndName("KAZ", "Kazakhstan"),
    LocationCodeAndName("KEN", "Kenya"),
    LocationCodeAndName("KIR", "Kiribati"),
    LocationCodeAndName("PRK", "Korea, Democratic People's Republic of"),
    LocationCodeAndName("KOR", "Korea, Republic of"),
    LocationCodeAndName("KWT", "Kuwait"),
    LocationCodeAndName("KGZ", "Kyrgyzstan"),
    LocationCodeAndName("LAO", "Lao People's Democratic Republic"),
    LocationCodeAndName("LVA", "Latvia"),
    LocationCodeAndName("LBN", "Lebanon"),
    LocationCodeAndName("LSO", "Lesotho"),
    LocationCodeAndName("LBR", "Liberia"),
    LocationCodeAndName("LBY", "Libya"),
    LocationCodeAndName("LIE", "Liechtenstein"),
    LocationCodeAndName("LTU", "Lithuania"),
    LocationCodeAndName("LUX", "Luxembourg"),
    LocationCodeAndName("MAC", "Macao"),
    LocationCodeAndName("MKD", "North Macedonia"),
    LocationCodeAndName("MDG", "Madagascar"),
    LocationCodeAndName("MWI", "Malawi"),
    LocationCodeAndName("MYS", "Malaysia"),
    LocationCodeAndName("MDV", "Maldives"),
    LocationCodeAndName("MLI", "Mali"),
    LocationCodeAndName("MLT", "Malta"),
    LocationCodeAndName("MHL", "Marshall Islands"),
    LocationCodeAndName("MTQ", "Martinique"),
    LocationCodeAndName("MRT", "Mauritania"),
    LocationCodeAndName("MUS", "Mauritius"),
    LocationCodeAndName("MYT", "Mayotte"),
    LocationCodeAndName("MEX", "Mexico"),
    LocationCodeAndName("FSM", "Micronesia, Federated States of"),
    LocationCodeAndName("MDA", "Moldova, Republic of"),
    LocationCodeAndName("MCO", "Monaco"),
    LocationCodeAndName("MNG", "Mongolia"),
    LocationCodeAndName("MNE", "Montenegro"),
    LocationCodeAndName("MSR", "Montserrat"),
    LocationCodeAndName("MAR", "Morocco"),
    LocationCodeAndName("MOZ", "Mozambique"),
    LocationCodeAndName("MMR", "Myanmar"),
    LocationCodeAndName("NAM", "Namibia"),
    LocationCodeAndName("NRU", "Nauru"),
    LocationCodeAndName("NPL", "Nepal"),
    LocationCodeAndName("NLD", "Netherlands"),
    LocationCodeAndName("ANT", "Netherlands Antilles"),
    LocationCodeAndName("NCL", "New Caledonia"),
    LocationCodeAndName("NZL", "New Zealand"),
    LocationCodeAndName("NIC", "Nicaragua"),
    LocationCodeAndName("NER", "Niger"),
    LocationCodeAndName("NGA", "Nigeria"),
    LocationCodeAndName("NIU", "Niue"),
    LocationCodeAndName("NFK", "Norfolk Island"),
    LocationCodeAndName("MNP", "Northern Mariana Islands"),
    LocationCodeAndName("NOR", "Norway"),
    LocationCodeAndName("OMN", "Oman"),
    LocationCodeAndName("PAK", "Pakistan"),
    LocationCodeAndName("PLW", "Palau"),
    LocationCodeAndName("PSE", "Palestine, State of"),
    LocationCodeAndName("PAN", "Panama"),
    LocationCodeAndName("PNG", "Papua New Guinea"),
    LocationCodeAndName("PRY", "Paraguay"),
    LocationCodeAndName("PER", "Peru"),
    LocationCodeAndName("PHL", "Philippines"),
    LocationCodeAndName("PCN", "Pitcairn"),
    LocationCodeAndName("POL", "Poland"),
    LocationCodeAndName("PRT", "Portugal"),
    LocationCodeAndName("PRI", "Puerto Rico"),
    LocationCodeAndName("QAT", "Qatar"),
    LocationCodeAndName("REU", "Réunion"),
    LocationCodeAndName("ROU", "Romania"),
    LocationCodeAndName("RUS", "Russian Federation"),
    LocationCodeAndName("RWA", "Rwanda"),
    LocationCodeAndName("BLM", "Saint Barthélemy"),
    LocationCodeAndName("SHN", "Saint Helena, Ascension and Tristan da Cunha"),
    LocationCodeAndName("KNA", "Saint Kitts and Nevis"),
    LocationCodeAndName("LCA", "Saint Lucia"),
    LocationCodeAndName("MAF", "Saint Martin (French part)"),
    LocationCodeAndName("SPM", "Saint Pierre and Miquelon"),
    LocationCodeAndName("VCT", "Saint Vincent and the Grenadines"),
    LocationCodeAndName("WSM", "Samoa"),
    LocationCodeAndName("SMR", "San Marino"),
    LocationCodeAndName("STP", "Sao Tome and Principe"),
    LocationCodeAndName("SAU", "Saudi Arabia"),
    LocationCodeAndName("SEN", "Senegal"),
    LocationCodeAndName("SRB", "Serbia"),
    LocationCodeAndName("SYC", "Seychelles"),
    LocationCodeAndName("SLE", "Sierra Leone"),
    LocationCodeAndName("SGP", "Singapore"),
    LocationCodeAndName("SVK", "Slovakia"),
    LocationCodeAndName("SVN", "Slovenia"),
    LocationCodeAndName("SLB", "Solomon Islands"),
    LocationCodeAndName("SOM", "Somalia"),
    LocationCodeAndName("ZAF", "South Africa"),
    LocationCodeAndName("SGS", "South Georgia and the South Sandwich Islands"),
    LocationCodeAndName("ESP", "Spain"),
    LocationCodeAndName("LKA", "Sri Lanka"),
    LocationCodeAndName("SDN", "Sudan"),
    LocationCodeAndName("SUR", "Suriname"),
    LocationCodeAndName("SJM", "Svalbard and Jan Mayen"),
    LocationCodeAndName("SWZ", "Eswatini"),
    LocationCodeAndName("SWE", "Sweden"),
    LocationCodeAndName("CHE", "Switzerland"),
    LocationCodeAndName("SYR", "Syrian Arab Republic"),
    LocationCodeAndName("TWN", "Taiwan, Province of China"),
    LocationCodeAndName("TJK", "Tajikistan"),
    LocationCodeAndName("THA", "Thailand"),
    LocationCodeAndName("TLS", "Timor-Leste"),
    LocationCodeAndName("TGO", "Togo"),
    LocationCodeAndName("TKL", "Tokelau"),
    LocationCodeAndName("TON", "Tonga"),
    LocationCodeAndName("TTO", "Trinidad and Tobago"),
    LocationCodeAndName("TUN", "Tunisia"),
    LocationCodeAndName("TUR", "Türkiye"),
    LocationCodeAndName("TKM", "Turkmenistan"),
    LocationCodeAndName("TCA", "Turks and Caicos Islands"),
    LocationCodeAndName("TUV", "Tuvalu"),
    LocationCodeAndName("UGA", "Uganda"),
    LocationCodeAndName("UKR", "Ukraine"),
    LocationCodeAndName("ARE", "United Arab Emirates"),
    LocationCodeAndName("GBR", "United Kingdom"),
    LocationCodeAndName("UMI", "United States Minor Outlying Islands"),
    LocationCodeAndName("URY", "Uruguay"),
    LocationCodeAndName("UZB", "Uzbekistan"),
    LocationCodeAndName("VUT", "Vanuatu"),
    LocationCodeAndName("VEN", "Venezuela, Bolivarian Republic of"),
    LocationCodeAndName("VNM", "Viet Nam"),
    LocationCodeAndName("VGB", "Virgin Islands, British"),
    LocationCodeAndName("VIR", "Virgin Islands, U.S."),
    LocationCodeAndName("WLF", "Wallis and Futuna"),
    LocationCodeAndName("ESH", "Western Sahara"),
    LocationCodeAndName("YEM", "Yemen"),
    LocationCodeAndName("ZMB", "Zambia"),
    LocationCodeAndName("ZWE", "Zimbabwe"),
    LocationCodeAndName("XX", "Unknown"),
]
