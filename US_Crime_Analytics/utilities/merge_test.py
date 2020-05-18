import pandas as pd

crime_90_15 = pd.read_csv(
    '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/crime_data/Crime_1990_2015_Req_Vars_Unique_Crosswalk_Merged_Arngd.csv')

crime_90_15_req_vars = crime_90_15[['ORI', 'AGENCY', 'Govt_level', 'place_fips', 'STATEFP']]
crime_90_15_req_vars.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/temp/crime_90_15_req_vars.csv', index=False)

# cen90 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/National_Census_1990_unique.csv')
# cen90_crime_merged = cen90.merge(crime_90_15_req_vars, on=['STATEFP', 'place_fips'])
#
# print(cen90_crime_merged.shape[0])

counties_00 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv')
cities_00 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_2000/new_census_variables/new_census_cities_townships_00_new_vars.csv')

cen00 = counties_00.append([cities_00])
pd.read_csv('')

cen00_crime_merged = cen00.merge(crime_90_15_req_vars, on=['STATEFP', 'place_fips'])
print(cen00_crime_merged.shape[0])


cen00_crime_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/temp/cen00_crime_merged.csv', index=False)


cen00_crime_merged = set(cen00_crime_merged['ORI'])

print(cen00_crime_merged.__len__())



arrests_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/arrests/Arrests_All_Race_1990_2016.xlsx')

r