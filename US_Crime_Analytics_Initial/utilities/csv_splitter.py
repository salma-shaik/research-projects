import pandas as pd
from main_census_merge.utilities import clean_files as cf
from main_census_merge.utilities import fips_codes_generator as fcg

"""
Splitting city and county census files to city/county, urban and rural respectively
"""


def split_csv(file_path, cen_type, cen_year, out_path):
    initial_csv_df = pd.read_csv(file_path)

    if cen_type == 'county':
        if cen_year == '00':
            county_df = initial_csv_df.head(3142)

        elif cen_year == '10':
            """
                upto 3145- county data
                3146 to 6288- urban data
                6289 to end - rural data

            """
            county_df = initial_csv_df.head(3144)

        cf.write_updated_df_file(county_df, out_path)
        # county_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann.csv', encoding='utf-8', index=False)
        #
        # county_urban_df = initial_csv_df.iloc[3143:6286]
        # county_urban_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county_urban.csv', encoding='utf-8', index=False)
        #
        # county_rural_df = initial_csv_df.iloc[6286:]
        # county_rural_df.to_csv('data/census_county_2010/DEC_10_SF1_P12_with_ann_county_rural.csv', encoding='utf-8', index=False)
    elif cen_type == 'city':
        if cen_year == '00':
            """
                upto 25152 row - city data
                25153 to 50302 - urban data
                50303 to end - rural data
            """
            city_df = initial_csv_df.head(25151)
        elif cen_year == '10':
            """
                upto 29263 - city data
                29264 to 58524 - urban data
                58525 to end - rural data

            """
            city_df = initial_csv_df.head(29262)
        cf.write_updated_df_file(city_df, out_path)

        # city_urban_df = initial_csv_df.iloc[29261:58522]
        # city_urban_df.to_csv('data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_urban.csv', encoding='utf-8', index=False)
        #
        # city_rural_df = initial_csv_df.iloc[58522:]
        # city_rural_df.to_csv('data/census_cities_2010/DEC_10_SF1_P12_with_ann_city_rural.csv', encoding='utf-8', index=False)
        #


fp_list = cf.find_census_files_path('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data', 'initial_files', 'reduced_census_files')

for fp in fp_list:
    in_path, ot_path = fp
    census_type, census_year = fcg.get_census_type_year(in_path)
    split_csv(in_path, census_type, census_year, ot_path)
