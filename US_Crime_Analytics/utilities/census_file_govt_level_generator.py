import pandas as pd

pd.options.mode.chained_assignment = None


def get_final_main_cgovtype_ori_agency(file_path):
    """
        Obtain ORI, AGENCY, CGOVTYPE, FIPS_STATE, FIPS_PLACE from final main(90-01) file
    """
    final_main_df = pd.read_csv(file_path)
    final_main_fips_ori_agency = final_main_df[['ORI', 'AGENCY', 'CGOVTYPE', 'FIPS_STATE', 'FIPS_PLACE']]

    """
    1. Obtain only unique records from the final main file - key: fips place + fips state
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency.drop_duplicates(['FIPS_STATE', 'FIPS_PLACE']) # --> 11,602 rows

    """
    2. Rename CGOVTYPE, FIPS_STATE, FIPS_PLACE to Govt_level, 'STATEFP', 'place_fips' to match national census file
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.rename(
        {'CGOVTYPE': 'Govt_level', 'FIPS_STATE': 'STATEFP', 'FIPS_PLACE': 'place_fips'}, axis='columns')

    """
    3. Get only those records from 90 final main file whose cgovtype is 1,2 or 3
    """
    final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.loc[final_main_fips_ori_agency_unique['Govt_level'].isin([1, 2, 3])]

    return final_main_fips_ori_agency_unique


def get_glevel_ori_agency(county_cens_file, crime_df, filename, cens_year, city_cens_file=False):

    """
        Merge CGOVTYPE, ORI, AGENCY from final main file into census files based on state and place fips.
    """

    """
    1. Append cities census file to counties census file
    """
    national_census_df = pd.read_csv(county_cens_file)

    """
        Checking for city census file coz we need to first append city census file to the bottom of county census file for 2000 and 2010.
        And city census file is passed only for 2000 and 2010 since for 1990 city and county census data is already together.
    """
    if city_cens_file:
        cities_df = pd.read_csv(city_cens_file)
        national_census_df = national_census_df.append([cities_df])
        national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/census/Census_{cens_year}.csv', index=False)

    print(f'{filename} before merging with crime file: ', national_census_df.shape[0])

    # Drop duplicates
    national_census_df = national_census_df.drop_duplicates(['STATEFP', 'place_fips'])
    national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/census/Census_{cens_year}_Unique.csv', index=False)
    print('national_census_df records after dropping duplicates: ', national_census_df.shape[0])

    """
    2.
    Merge national all census files with 1990 final main file to get the correct cgovtype, CNTY based on fips state, fips place. 
    Also obtain ORI, Agency columns from final main file. The census files sent to this merge don't have ORI, AGENCY columns
    Inner join coz we want only those agencies that are present in both the files so that we can analyze agencies that have data consistently over time    
    """
    national_census_df = national_census_df.merge(crime_df, on=['STATEFP', 'place_fips'], how='right')
    #national_census_df = national_census_df.merge(crime_df, on=['STATEFP', 'place_fips'], how='outer')
    #national_census_df = national_census_df.merge(crime_df, on=['STATEFP', 'place_fips'])

    print(f'{filename} after merging with crime: ', national_census_df.shape[0])


    """
    3. Create final Govt_level = Govt_level_y column which has govt_level values from final main file and get rid of _x and _y columns 
    """
    national_census_df['Govt_level'] = national_census_df['Govt_level_y']
    national_census_df['CNTY'] = national_census_df['CNTY_y']
    national_census_df.drop(['Govt_level_x', 'Govt_level_y', 'CNTY_x', 'CNTY_y'], axis=1, inplace=True)

    """
    Add the year column to have year for even the missing census rows for certain ORIs
    """
    national_census_df['YEAR'] = cens_year

    """
    4. Rearrange columns so that ORI, AGENCY, Govt_level are at the beginning
    """
    cols = list(national_census_df.columns.values)
    cols.pop(cols.index('ORI'))
    cols.pop(cols.index('AGENCY'))
    cols.pop(cols.index('Govt_level'))
    cols.pop(cols.index('CNTY'))
    cols.pop(cols.index('YEAR'))

    national_census_df = national_census_df[['ORI', 'AGENCY', 'Govt_level', 'CNTY', 'YEAR'] + cols]
    #national_census_df = national_census_df[['ORI', 'AGENCY', 'YEAR'] + cols]

    # write the final df with updated govt_level, ori, agency etc. to a csv
    national_census_df.to_csv(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/{filename}.csv', index=False)


def merge_cen_final_main():
    """
        Use the Crime_National_UCR_offenses_1990_2015_Req_Vars_Unique_Crosswalk_Merged_CGOVTYPE123.csv
    """
    crime_major = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/Crime_Unique_Crswlk_Major_Merged_Inner.csv')

    crime_major_gov_fips = crime_major[['ORI', 'AGENCY', 'Govt_level', 'place_fips', 'STATEFP', 'CNTY']]
    crime_major_gov_fips.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crime/Crime_Major_Gov_Fips.csv', index=False)
    print('crime_90_15_req_vars length: ', crime_major_gov_fips.shape[0])

    # Create the final national census 2000 file by combining 2000 cities and counties. Then merge it with crime main df on place and state fips
    counties_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv'
    cities_00_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_cities_2000/new_census_variables/new_census_cities_townships_00_new_vars.csv'
    #get_glevel_ori_agency(county_cens_file=counties_00_file, city_cens_file=cities_00_file,crime_df=crime_major_gov_fips, filename='Census_2000_Crime_Merge_Outer', cens_year=2000)
    #get_glevel_ori_agency(county_cens_file=counties_00_file, city_cens_file=cities_00_file, crime_df=crime_major_gov_fips, filename='Census_2000_Crime_Merge_Right', cens_year = 2000)
    #get_glevel_ori_agency(county_cens_file=counties_00_file, city_cens_file=cities_00_file, crime_df=crime_major_gov_fips, filename='Census_2000_Crime_Merge_Inner', cens_year = 2000)


    # Create the final national census 2010 file by merging combining 2010 cities and counties.
    counties_10_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv'
    cities_10_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_cities_2010/new_census_variables/new_census_cities_townships_10_new_vars.csv'
    #get_glevel_ori_agency(county_cens_file=counties_10_file, city_cens_file=cities_10_file,crime_df=crime_major_gov_fips, filename='Census_2010_Crime_Merge_Outer', cens_year=2010)
    # get_glevel_ori_agency(county_cens_file=counties_10_file, city_cens_file=cities_10_file, crime_df=crime_major_gov_fips, filename='Census_2010_Crime_Merge_Right', cens_year = 2010)
    #get_glevel_ori_agency(county_cens_file=counties_10_file, city_cens_file=cities_10_file, crime_df=crime_major_gov_fips, filename='Census_2010_Crime_Merge_Inner', cens_year = 2010)


    """
        # Clean up 1990 census file
    """
    # national_cens_90_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/National_Census_1990_All_Initial.xlsx')
    #
    # # drop the duplicates based on state and place fips
    # national_cens_90_df_unique = national_cens_90_df.drop_duplicates(['STATEFP', 'place_fips'])
    #
    # # add YEAR column with 1990 value at 5th position
    # national_cens_90_df_unique.insert(5, 'YEAR', 1990)
    #
    # # Rename Hispan columns to Hispanic
    # national_cens_90_df_unique.rename({'Hispan_allcount': 'Hispanic_count', 'Hispan_Males_All': 'Hispanic_Males_All', 'Age1524_HispanM': 'Age1524_HispanicM', 'Age1524_HispanF': 'Age1524_HispanicF', 'Hispan_Females_All': 'Hispanic_Females_All'}, inplace=True, axis=1)
    #
    # # drop 'other' columns
    # national_cens_90_df_unique.drop(['Other_count', 'Other_Males_All', 'Age1524_OtherM', 'Age1524_OtherF', 'Other_Females_All'], inplace=True, axis=1)
    #
    # national_cens_90_df_unique.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/National_Census_1990_unique.csv', index=False)

    # Create the final 1990 census file by merging with 90 final main file
    #get_glevel_ori_agency(county_cens_file='/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/National_Census_1990_unique.csv',crime_df=crime_major_gov_fips, filename='Census_1990_Crime_Merge_Outer', cens_year=1990)
    get_glevel_ori_agency(county_cens_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/National_Census_1990_unique.csv', crime_df = crime_major_gov_fips, filename = 'Census_1990_Crime_Merge_Right', cens_year = 1990)
    #get_glevel_ori_agency(county_cens_file = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/National_Census_1990_unique.csv', crime_df = crime_major_gov_fips, filename = 'Census_1990_Crime_Merge_Inner', cens_year = 1990)


def normalize_cen_files():

    # There were some duplicates
    nat_cen_90 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/Census_1990_crime_merge.csv')
    nat_cen_90 = nat_cen_90.drop_duplicates(['ORI'])
    print('nat_cen_90 records after dropping duplicates: ', nat_cen_90.shape[0])

    nat_cen_00 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/Census_2000_crime_merge.csv')
    nat_cen_00 = nat_cen_00.drop_duplicates(['ORI'])
    print('nat_cen_00 records after dropping duplicates: ', nat_cen_00.shape[0])

    nat_cen_10 = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/Census_2010_crime_merge.csv')
    nat_cen_10 = nat_cen_10.drop_duplicates(['ORI'])
    print('nat_cen_10 records after dropping duplicates: ', nat_cen_10.shape[0])

    nat_cen_common_ori = set(nat_cen_90['ORI']).intersection(set(nat_cen_00['ORI']), set(nat_cen_10['ORI']))
    print('nat_cen_common_ori: ', nat_cen_common_ori.__len__())

    nat_cen_common_ori_df = pd.DataFrame(list(nat_cen_common_ori), columns=['ORI'])

    nat_cen_common_ori_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/nat_cen_common_ori.csv', index=False)

    nat_cen_10_normalized = nat_cen_10.merge(nat_cen_common_ori_df)
    nat_cen_10_normalized.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/Census_2010_Normalized.csv', index=False)
    print('nat_cen_10_normalized len: ', nat_cen_10_normalized.shape[0])

    nat_cen_00_normalized = nat_cen_00.merge(nat_cen_common_ori_df)
    nat_cen_00_normalized.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/Census_2000_Normalized.csv', index=False)
    print('nat_cen_00_normalized len: ', nat_cen_00_normalized.shape[0])

    nat_cen_90_normalized = nat_cen_90.merge(nat_cen_common_ori_df)
    nat_cen_90_normalized.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/Census_1990_Normalized.csv', index=False)
    print('nat_cen_90_normalized len: ', nat_cen_90_normalized.shape[0])

def consolidate_all_census_files():

    # Finally, read all the years' census files to append together and form a consolidated census file with updated govt level, ORI from the 1990 final main file
    # nat_cen_90_df = pd.read_csv(
    #     '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_1990_Crime_Merge_Right.csv')

    nat_cen_90_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/census_cities_1990/new_census_variables/cen_90_ini_cnty_city_new_twnshp_glevels.csv')
    nat_cen_00_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_2000_Crime_Merge_Right.csv')
    nat_cen_10_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_2010_Crime_Merge_Right.csv')

    # Append all the census files together
    nat_cen_all = nat_cen_10_df.append([nat_cen_00_df, nat_cen_90_df], sort=False)

    nat_cen_all.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime_All_Right.csv', index=False)

    """
        Sort the df by 'ORI' and 'YEAR' to get the 3 occurences of each ORI together and then sort by YEAR(10,00,90)
    """
    nat_cen_all_sorted = nat_cen_all.sort_values(by=['ORI', 'YEAR'], ascending=[True, False])

    # ############## Check this out
    # Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
    nat_cen_all_sorted = nat_cen_all_sorted.reset_index(drop=True)

    """
        Write the above sorted df to a csv for future use and reference
    """
    nat_cen_all_sorted.to_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime_All_Right_Sorted.csv',
        index=False)

    print('nat_cen_all_sorted length ', nat_cen_all_sorted.shape[0])

"""
   Merge each of the final 90, 00 and 10 the census files with final main file to get correct govt level values
   """
# merge_cen_final_main()


"""
   Perform 3 way merge on the census files to have uniform ORIs and st+place fips throughout
   """
# normalize_cen_files()


"""
    Consolidate all the final census files with the updated ORIs together
"""
consolidate_all_census_files()