import pandas as pd

def cen_90_crime_unmatched():
    cens_90_crime_outer=pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Census_1990_Crime_Merge_Outer_Unmatched_Test.csv')

    # Get the umatched census records
    cens_90_unmatched_with_crime = cens_90_crime_outer[cens_90_crime_outer.ORI.isnull()]
    cens_90_unmatched_with_crime = cens_90_unmatched_with_crime.dropna(how='all', axis='columns')
    cens_90_unmatched_with_crime['CNTY_cen'] = cens_90_unmatched_with_crime['CNTY_x']
    cens_90_unmatched_with_crime.drop(['CNTY_x'], axis=1, inplace=True)
    cens_90_unmatched_with_crime['plname_4chars'] = cens_90_unmatched_with_crime['placename'].map(lambda placename: placename[:4])
    cens_90_unmatched_with_crime.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Census_1990_Unmatched_With_Crime.csv', index=False)
    cens_90_unmatched_with_crime.sort_values(by=['STATEFP', 'CNTY_cen','plname_4chars'], inplace=True)


    # Get the unmatched crime records
    crime_unmatched_with_cen_90 = cens_90_crime_outer[cens_90_crime_outer.placename.isnull()]
    crime_unmatched_with_cen_90 = crime_unmatched_with_cen_90.dropna(how='all', axis='columns')
    crime_unmatched_with_cen_90['agency_4chars'] = crime_unmatched_with_cen_90['AGENCY'].map(lambda AGENCY: AGENCY[:4])
    crime_unmatched_with_cen_90['CNTY_crime'] = crime_unmatched_with_cen_90['CNTY_y']
    crime_unmatched_with_cen_90.drop(['CNTY_y'], axis=1, inplace=True)
    crime_unmatched_with_cen_90.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_1990.csv', index=False)
    crime_unmatched_with_cen_90.sort_values(by=['STATEFP', 'CNTY_crime', 'agency_4chars'], inplace=True)

    # convert placename and agency to lowercase to be able to merge ignoring case
    cens_90_unmatched_with_crime['plname_4chars'] = cens_90_unmatched_with_crime['plname_4chars'].str.lower()
    crime_unmatched_with_cen_90['agency_4chars'] = crime_unmatched_with_cen_90['agency_4chars'].str.lower()

    # merge these 2 unmatched crime and census files on  state fips, cnty fips and place/agency 4 chars
    census_90_crime_unmatched_merge = cens_90_unmatched_with_crime.merge(crime_unmatched_with_cen_90, left_on=['STATEFP', 'CNTY_cen','plname_4chars'], right_on=['STATEFP', 'CNTY_crime', 'agency_4chars'])
    census_90_crime_unmatched_merge.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/census_90_crime_unmatched_merge.csv', index=False)


def crime_cen_00_unmatched():
    cens_00_crime_outer = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Census_2000_Crime_Merge_Outer.csv')
    crime_unmatched_with_cen_00 = cens_00_crime_outer[cens_00_crime_outer.placename.isnull()]
    crime_unmatched_with_cen_00 = crime_unmatched_with_cen_00.dropna(how='all', axis='columns')
    crime_unmatched_with_cen_00.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_2000.csv', index=False)
    crime_unmatched_with_cen_00.sort_values(by=['STATEFP', 'CNTY'], inplace=True)


def crime_cen_10_unmatched():
    cens_10_crime_outer = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Census_2010_Crime_Merge_Outer.csv')
    crime_unmatched_with_cen_10 = cens_10_crime_outer[cens_10_crime_outer.placename.isnull()]
    crime_unmatched_with_cen_10 = crime_unmatched_with_cen_10.dropna(how='all', axis='columns')
    crime_unmatched_with_cen_10.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/merge_files/census_crime/Crime_Unmatched_With_Census_2010.csv',
        index=False)
    crime_unmatched_with_cen_10.sort_values(by=['STATEFP', 'CNTY'], inplace=True)


"""
    Census 1990 api check
"""
def check_cen_90_api_crime_merge():
    crime_major = pd.read_csv('C:/Users/arvind1613/OneDrive/Desktop/General/Projects/main_census_merge/data/merge_files/Crime_Unique_Crswlk_Major_Merged_Inner.csv')
    print('crime_major: ', crime_major.shape[0])

    cen_county_90 = pd.read_csv('C:/Users/arvind1613/OneDrive/Desktop/General/Projects/main_census_merge/data/census_county_1990/census_counties_1990.csv')
    cen_county_90_req = cen_county_90[['place_fips','placename','CNTY','STATEFP']]

    cen_city_90 = pd.read_csv('C:/Users/arvind1613/OneDrive/Desktop/General/Projects/main_census_merge/data/census_cities_1990/new_census_townships_90_initial.csv')
    cen_city_90_req = cen_city_90[['ANPSADPI', 'state',	'county', 'county subdivision']]

    cen_city_90_req = cen_city_90_req.rename({'state':'STATEFP', 'county':'CNTY', 'county subdivision':'place_fips', 'ANPSADPI':'placename'}, axis='columns')

    cen_90 = cen_county_90_req.append([cen_city_90_req], sort=False)

    cen_90.to_csv('C:/Users/arvind1613/OneDrive/Desktop/General/Projects/main_census_merge/data/cen_90_test.csv', index=False)
    print('cen_90 ', cen_90.shape[0])

    cen_crime_merged = cen_90.merge(crime_major, on=['STATEFP', 'place_fips'])
    print('crime_cen_merged ', cen_crime_merged.shape[0])

    cen_crime_merged.to_csv('C:/Users/arvind1613/OneDrive/Desktop/General/Projects/main_census_merge/data/cen_90_inner_merge_test.csv', index=False)


crime_cen_00_unmatched()

crime_cen_10_unmatched()