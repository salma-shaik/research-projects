import pandas as pd

"""
    Get the Crime_National_UCR_offenses_1990_2015_Req_Vars_Unique_Crosswalk_Merged_CGOVTYPE123 file
    Get only the reqd columns - 'ORI', 'AGENCY', 'Govt_level', 'STATEFP', 'place_fips'
"""

def get_reqd_crime_df(crime_fl_path):
    crime_df = pd.read_csv(crime_fl_path)
    crime_reqd_df = crime_df[['ORI', 'AGENCY', 'Govt_level', 'STATEFP', 'place_fips']]
    # crime_reqd_df records 16771
    crime_reqd_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/crime_data/Crime_90_15_req_vars_census_glevel.csv', index=False)
    return crime_reqd_df

crime_reqd_vars_df = get_reqd_crime_df('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/crime_data/Crime_National_UCR_offenses_1990_2015_Req_Vars_Unique_Crosswalk_Merged_CGOVTYPE123.csv')


"""
    Merge Crime_90_15_req_vars_census_glevel.csv with each of the census files on fips place and state to get correct cgovtype in census files
"""


def get_cgovtype_for_census(crime_df):
    pass