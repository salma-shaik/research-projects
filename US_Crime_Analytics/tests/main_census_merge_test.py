import pandas as pd

"""
'''
To disable the warning - SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame
The point of the SettingWithCopyWarning is to show users (and esp new users) that they may be operating on a copy and not the original as they think. 
These are False positives (you know what you are doing, so it ok). One possibility is simply to turn off the (by default warn)
'''
pd.options.mode.chained_assignment = None  # default='warn'

main_file_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/Final_Main_Var_1990_2001.csv')
main_file_df_subset = main_file_df.iloc[:24]

county_census_2010_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann.csv')
county_census_2010_df_subset = county_census_2010_df.iloc[[69, 74, 81]]
county_census_2010_df_subset.rename({'Total:':'Total'}, axis=1, inplace=True)

for row in county_census_2010_df_subset.itertuples():
    print(getattr(row, 'Id2'))
    print(getattr(row,'Total'))

# get the last occurence of matching STCO_FIPS for a given Id2 so that new record with year 2010 and Total: can be inserted below that

"""
main_file_snippet_df= pd.DataFrame(pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/main_file_snippet.csv'))
county_census_2010_snippet_df = pd.DataFrame(pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/2010_county_census_snippet.csv'))

# county_census_2010_snippet_req_df = county_census_2010_snippet_df[['FIPS_STATE', 'FIPS_COUNTY', 'YEAR', 'County_Census_Pop']]
merged_main_df = main_file_snippet_df.merge(county_census_2010_snippet_df, on=['FIPS_STATE', 'FIPS_COUNTY', 'YEAR'], how='outer')
merged_main_df.to_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/merged_main_file_snippet.csv', encoding='utf-8', index=False)
print(merged_main_df)