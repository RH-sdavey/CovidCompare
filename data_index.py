from covid19dh import covid19


class DataIndex:

    def __init__(self):
        self.covid_dataset, self.covid_datasource = covid19(verbose=False)
        self.all_countries_long = [
            'Saint Lucia', 'Guatemala', 'Guyana', 'Italy', 'Belize', 'Isle of Man',
            'Wallis and Futuna', 'Belarus', 'Solomon Islands', 'Libya', 'Gambia', 'Haiti',
            'Oman', 'San Marino', 'Uzbekistan', 'Cameroon', 'Turks and Caicos Islands',
            'El Salvador', 'Ecuador', 'Albania', 'Nicaragua', 'Singapore', 'Martinique',
            'Guam', 'Bahamas', 'Myanmar', 'Nepal', 'Bangladesh', 'Zambia', 'Lithuania',
            'Guinea-Bissau', 'Malawi', 'Greenland', 'Belgium', 'Syria', 'Tajikistan',
            'Botswana', 'Hong Kong', 'Mozambique', 'Estonia', 'Norway', 'Ireland',
            'Portugal', 'Jordan', 'South Sudan', 'Kosovo', 'Korea, South', 'Tonga', 'Spain',
            'Grenada', 'Zimbabwe', 'Iceland', 'Mexico', 'Latvia', 'Rwanda', 'Namibia',
            'French Polynesia', 'Sweden', 'Saudi Arabia', 'Mauritania', 'Jamaica',
            'Jersey', 'Germany', 'Malaysia', 'Yemen', 'Kuwait', 'Cook Islands', 'Iraq',
            'Puerto Rico', 'Papua New Guinea', 'Seychelles', 'Nauru', 'American Samoa',
            'Qatar', 'Burundi', 'Moldova', 'Congo', 'Micronesia', 'Holy See', 'Armenia',
            'Eritrea', 'Samoa', 'Uruguay', 'Paraguay', 'Costa Rica', 'Palestine',
            'United States', 'Brazil', 'Réunion', 'Denmark', 'United Arab Emirates',
            'Mongolia', 'France', 'Ukraine', 'Vanuatu', 'Chad',
            'Saint Helena, Ascension and Tristan da Cunha', 'Timor-Leste', 'Guinea',
            'Palau', 'Finland', 'Nigeria', 'Falkland Islands (Malvinas)', 'Bahrain',
            'Gibraltar', 'Virgin Islands, U.S.', "Cote d'Ivoire", 'Ethiopia', 'Uganda',
            'Burkina Faso', 'Egypt', 'Luxembourg', 'China', 'Sao Tome and Principe',
            'Austria', 'Kiribati', 'Guernsey', 'Saint Vincent and the Grenadines',
            'New Caledonia', 'Mali', 'Philippines', 'Lebanon', 'Bosnia and Herzegovina',
            'Tanzania', 'Turkey', 'Angola', 'Hungary', 'Tuvalu', 'French Guiana', 'Bermuda',
            'Cuba', 'Suriname', 'Dominica', 'United Kingdom', 'Togo', 'Azerbaijan', 'Algeria',
            'Chile', 'Sierra Leone', 'Czech Republic', 'Marshall Islands', 'Afghanistan',
            'Liberia', 'Tunisia', 'Bhutan', 'Romania', 'Tokelau', 'Equatorial Guinea',
            'Madagascar', 'Central African Republic', 'Gabon', 'Canada',
            'Dominican Republic', 'Taiwan', 'Vietnam', 'Lesotho', 'Comoros',
            'Bonaire, Sint Eustatius and Saba', 'Saint Kitts and Nevis', 'Slovenia',
            'Greece', 'Cayman Islands', 'Somalia', 'Argentina', 'Swaziland', 'Montenegro',
            'South Africa', 'Panama', 'Sint Maarten', 'Morocco', 'Faroe Islands',
            'North Macedonia', 'Georgia', 'Kazakhstan', 'Slovakia', 'Barbados', 'Honduras',
            'Kenya', 'India', 'Iran', 'Pakistan', 'Peru', 'Poland', 'Sudan', 'Israel',
            'Sri Lanka', 'Brunei', 'Benin', 'Andorra', 'Maldives', 'Montserrat', 'Senegal',
            'Cyprus', 'Djibouti', 'Niger', 'Fiji', 'Turkmenistan', 'Laos',
            'Congo, the Democratic Republic of the', 'Croatia', 'Venezuela',
            'Bolivia', 'Indonesia', 'Colombia', 'Mayotte', 'Serbia',
            'Macao', 'Northern Mariana Islands', 'Guadeloupe', 'Niue', 'Curacao',
            'Antigua and Barbuda', 'Aruba', 'New Zealand', 'Monaco', 'Australia',
            'Cape Verde', 'Bulgaria', 'Malta', 'Kyrgyzstan', 'Virgin Islands, British',
            'Mauritius', 'Ghana', 'Switzerland', 'Cambodia', 'Trinidad and Tobago',
            'Thailand', 'Anguilla', 'Netherlands', 'Japan', 'Russia', 'Liechtenstein',
        ]

        self.all_countries_short = [
            'LCA', 'GTM', 'GUY', 'ITA', 'BLZ', 'IMN', 'WLF', 'BLR', 'SLB', 'LBY', 'GMB', 'HTI',
            'OMN', 'SMR', 'UZB', 'CMR', 'TCA', 'SLV', 'ECU', 'ALB', 'NIC', 'SGP', 'MTQ', 'GUM',
            'BHS', 'MMR', 'NPL', 'BGD', 'ZMB', 'LTU', 'GNB', 'MWI', 'GRL', 'BEL', 'SYR', 'TJK',
            'BWA', 'HKG', 'MOZ', 'EST', 'NOR', 'IRL', 'PRT', 'JOR', 'SSD', 'RKS', 'KOR', 'TON',
            'ESP', 'GRD', 'ZWE', 'ISL', 'MEX', 'LVA', 'RWA', 'NAM', 'PYF', 'SWE', 'SAU', 'MRT',
            'JAM', 'JEY', 'DEU', 'MYS', 'YEM', 'KWT', 'COK', 'IRQ', 'PRI', 'PNG', 'SYC', 'NRU',
            'ASM', 'QAT', 'BDI', 'MDA', 'COG', 'FSM', 'VAT', 'ARM', 'ERI', 'WSM', 'URY', 'PRY',
            'CRI', 'PSE', 'USA', 'BRA', 'REU', 'DNK', 'ARE', 'MNG', 'FRA', 'UKR', 'VUT', 'TCD',
            'SHN', 'TLS', 'GIN', 'PLW', 'FIN', 'NGA', 'FLK', 'BHR', 'GIB', 'VIR', 'CIV', 'ETH',
            'UGA', 'BFA', 'EGY', 'LUX', 'CHN', 'STP', 'AUT', 'KIR', 'GGY', 'VCT', 'NCL', 'MLI',
            'PHL', 'LBN', 'BIH', 'TZA', 'TUR', 'AGO', 'HUN', 'TUV', 'GUF', 'BMU', 'CUB', 'SUR',
            'DMA', 'GBR', 'TGO', 'AZE', 'DZA', 'CHL', 'SLE', 'CZE', 'MHL', 'AFG',
            'LBR', 'TUN', 'BTN', 'ROU', 'TKL', 'GNQ', 'MDG', 'CAF', 'GAB', 'CAN', 'DOM', 'TWN',
            'VNM', 'LSO', 'COM', 'BES', 'KNA', 'SVN', 'GRC', 'CYM', 'SOM', 'ARG', 'SWZ', 'MNE',
            'ZAF', 'PAN', 'SXM', 'MAR', 'FRO', 'MKD', 'GEO', 'KAZ', 'SVK', 'BRB', 'HND', 'KEN',
            'IND', 'IRN', 'PAK', 'PER', 'POL', 'SDN', 'ISR', 'LKA', 'BRN', 'BEN', 'AND', 'MDV',
            'MSR', 'SEN', 'CYP', 'DJI', 'NER', 'FJI', 'TKM', 'LAO', 'COD', 'HRV', 'VEN', 'BOL',
            'IDN', 'COL', 'MYT', 'SRB', 'MAC', 'MNP', 'GLP', 'NIU', 'CUW', 'ATG', 'ABW', 'NZL',
            'MCO', 'AUS', 'CPV', 'BGR', 'MLT', 'KGZ', 'VGB', 'MUS', 'GHA', 'CHE', 'KHM', 'TTO',
            'THA', 'AIA', 'NLD', 'JPN', 'RUS', 'LIE'
        ]

        self.all_countries_zip_iter = zip(self.all_countries_short, self.all_countries_long)
        self.all_countries_zipped_dict = dict(self.all_countries_zip_iter)
        self.sorted_all_countries_zip_dict = dict(sorted(self.all_countries_zipped_dict.items(), key=lambda x: x[0].lower()))

        self.all_columns = [
            'id', 'date', 'confirmed', 'deaths', 'recovered', 'tests', 'vaccines',
            'people_vaccinated', 'people_fully_vaccinated', 'hosp', 'icu', 'vent',
            'school_closing', 'workplace_closing', 'cancel_events',
            'gatherings_restrictions', 'transport_closing',
            'stay_home_restrictions', 'internal_movement_restrictions',
            'international_movement_restrictions', 'information_campaigns',
            'testing_policy', 'contact_tracing', 'facial_coverings',
            'vaccination_policy', 'elderly_people_protection',
            'government_response_index', 'stringency_index',
            'containment_health_index', 'economic_support_index',
            'administrative_area_level', 'administrative_area_level_1',
            'administrative_area_level_2', 'administrative_area_level_3',
            'latitude', 'longitude', 'population', 'iso_alpha_3', 'iso_alpha_2',
            'iso_numeric', 'iso_currency', 'key_local', 'key_google_mobility',
            'key_apple_mobility', 'key_jhu_csse', 'key_nuts', 'key_gadm'
        ]

        self.tab1_datatable_headers = ['Country', 'Population', 'Confirmed', 'Deaths', 'Recovered', 'Tests', 'Vaccines']
        self.tab1_datatable_keys = ['key_gadm', 'population', 'confirmed', 'deaths', 'recovered', 'tests', 'vaccines']

