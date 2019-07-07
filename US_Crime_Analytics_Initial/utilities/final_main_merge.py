import pandas as pd
import numpy as np

"""
def get_crime_records_with_census_oris(crime_fl, cen_ori):
    crime_ini_df = pd.read_csv(crime_fl)
 
    # Sort the df by ori_code and year to get all the occurences of each ORI together and then sort by YEAR(10,00,90)
  
    crime_ini_df_sorted = crime_ini_df.sort_values(by=['ori_code', 'year'], ascending=[True, False])

    crime_ini_df_sorted.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/Crime_Req_Vars_Sorted.csv', index=False)

    cen_ori = pd.read_csv(cen_ori)

    crime_filtered_cen_ori = crime_ini_df_sorted[crime_ini_df_sorted.ori_code.isin(cen_ori['ORI'])]

    crime_filtered_cen_ori.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/Crime_Req_Vars_Sorted_Filtered_Cen_ORI.csv', index=False)

    return crime_filtered_cen_ori

crime_df = get_crime_records_with_census_oris('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/Crime_1990_2015_Req_Vars.csv',
                                              '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/nat_cen_common_ori.csv')
                                              
"""


def merge_census_crime():
    """
    Census Columns:
        ORI	AGENCY	placename	Govt_level	place_fips	STATEFP	CNTY	YEAR
        POP100	White_count	Black_count	Hispanic_count	Age1524_WhiteM	White_Males_All
        Age1524_WhiteF	White_Females_All	Age1524_BlackM	Black_Males_All	Age1524_BlackF
        Black_Females_All	Hispanic_Males_All	Age1524_HispanicM	Age1524_HispanicF	Hispanic_Females_All
        Pct_WYM	Pct_WYF

    US_Crime_Analysis Columns:
        state	ori_code	group_number	division	year
        city_number	months_reported
        agency_name	agency_state	zip_code	murder	manslaughter	rape	robbery
        gun_robbery	knife_robbery	aggravated_assault	gun_assault	knife_assault	simple_assault
        burglary	larceny	auto_theft	officers_assaulted	officers_killed_by_felony
        officers_killed_by_accident	sub_group	population
    """
    census_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/interpolated_files/Census_Interpolated.csv')
    crime_df = pd.read_csv(
        '/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/final_crime_for_merge.csv')

    """
    Merge crime file with census file. Left merge for now to have all the ORIs and years from census file.
    Merging on ori and year
    """
    census_crime_merged = census_df.merge(crime_df, left_on=['ORI', 'YEAR'], right_on=['ORI', 'crime_year'], how='left')
    census_crime_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime_Merged.csv', index=False)
    # total rows in the merged file should have 385606 records equal to the ones in census


#merge_census_crime()

"""
    	AGENCY	placename	Govt_level	place_fips	STATEFP	CNTY		
    POP100	White_count	Black_count	Hispanic_count	Age1524_WhiteM	White_Males_All	
    Age1524_WhiteF	White_Females_All	Age1524_BlackM	Black_Males_All	Age1524_BlackF	
    Black_Females_All	Hispanic_Males_All	Age1524_HispanicM	Age1524_HispanicF	
    Hispanic_Females_All	Pct_WYM	Pct_WYF	
    
    state	ori_code	group_number	
    division		city_number	months_reported	agency_name		
    zip_code	murder	manslaughter	rape	robbery	gun_robbery	knife_robbery	
    aggravated_assault	gun_assault	knife_assault	simple_assault	burglary	
    larceny	auto_theft	officers_assaulted	officers_killed_by_felony	
    officers_killed_by_accident	sub_group	population
    
    Drop - ori_code, agency_state, year (since crime data is missing for some years) so will have identifiers from census file
"""


def clean_census_crime_merge_file():
    cen_cr_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime_Merged.csv')

    #cen_cr_df['state_abbr'] = cen_cr_df.ori_code

    # Some ORIs for some years are missing coz not all agencies have reported crime for all the years.
    # So need to bypass those using na_action='ignore' otherwise can't substring NA error
    cen_cr_df['state_abbr'] = cen_cr_df['ORI'].map(lambda ORI: ORI[:2], na_action='ignore')
    #cen_cr_df = cen_cr_df.rename({'year':'crime_year'}, axis='columns')

    cen_cr_df.drop(['agency_state', 'ORI.1'], axis=1, inplace=True)

    """
        Create the below new crime columns for basic analysis
        total_crime = sum(murder,manslaughter,rape,robbery,gun_robbery,knife_robbery,aggravated_assault,gun_assault,knife_assault,simple_assault,burglary,larceny,auto_theft)
        violent_crime = sum(murder,manslaughter,rape,robbery,aggravated_assault)
        property_crime = sum(burglary,larceny,auto_theft)
        crimes_against_officers = sum(officers_assaulted, officers_killed_by_felony)
        officers_killed_by_accident - not considering a crime. Is that right? Does the homicide data include these stats as well? If yes, then all 3 or just the 1st 2?
    """
    cen_cr_df['total_crime'] = cen_cr_df[['murder','manslaughter','rape','robbery','gun_robbery','knife_robbery','aggravated_assault',
                                          'gun_assault','knife_assault','simple_assault','burglary','larceny','auto_theft']].sum(axis=1)
    cen_cr_df['violent_crime'] = cen_cr_df[['murder', 'manslaughter', 'rape', 'robbery', 'aggravated_assault']].sum(axis=1)
    cen_cr_df['property_crime'] = cen_cr_df[['burglary','larceny','auto_theft']].sum(axis=1)
    cen_cr_df['crimes_against_officers'] = cen_cr_df[['officers_assaulted', 'officers_killed_by_felony']].sum(axis=1)

    cen_cr_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime.csv', index=False)


#clean_census_crime_merge_file()


def merge_census_crime_bea():
    cen_cr_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime/Census_Crime.csv')
    bea_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/economic/bea_census_all_1990_2015_cols_updated.csv')

    """
        # left merge on cen_cr to have all the ORIs, census records and to identify missing economic data if needed
        # bea cols(right) = year	fips_state	fips_county; cen_cr columns(left) = STATEFP	CNTY	YEAR
    """
    cen_cr_bea_merge = cen_cr_df.merge(bea_df, left_on=['STATEFP', 'CNTY', 'YEAR'], right_on=['fips_state', 'fips_county', 'year'], how='left')
    cen_cr_bea_merge.drop(['fips_state', 'fips_county', 'year'], axis=1, inplace=True)
    cen_cr_bea_merge.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea/Census_Crime_BEA.csv', index=False)


#merge_census_crime_bea()


def merge_cen_cr_bea_spatial():
    cen_cr_bea_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea/Census_Crime_BEA.csv')
    spatial_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/spatial_data/crime_coord_final_1990_2001.csv')

    # Get only the required columns from spatial df: ori, PRIMARY_LATITUDE	, PRIMARY_LONGITUDE, old_lat, old_long
    spatial_df_req_cols = spatial_df[['ori', 'PRIMARY_LATITUDE', 'PRIMARY_LONGITUDE', 'old_lat', 'old_long']]

    spatial_df_req_cols.drop_duplicates(subset=['ori'], inplace=True)

    # Left merge on ori to have all cen_cr_bea_df records.
    # on:- cen_cr_bea(left)- 'ORI_Census'; spatial(right) - 'ORI_Spatial';
    cen_cr_bea_spatial_merged = cen_cr_bea_df.merge(spatial_df_req_cols, left_on='ORI', right_on='ori', how='left')
    cen_cr_bea_spatial_merged.drop(['ori'], axis=1, inplace=True)
    cen_cr_bea_spatial_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial/Census_Crime_BEA_Spatial.csv', index=False)

    # Identify the agencies which don't have either PRIMARY or old or both spatial data
    cen_cr_bea_spatial_merged_missing = cen_cr_bea_spatial_merged[cen_cr_bea_spatial_merged.PRIMARY_LATITUDE.isnull()| cen_cr_bea_spatial_merged.PRIMARY_LONGITUDE.isnull() |
                                                          cen_cr_bea_spatial_merged.old_lat.isnull() | cen_cr_bea_spatial_merged.old_long.isnull()]
    cen_cr_bea_spatial_merged_missing.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial/Census_Crime_BEA_Spatial_SpatialMissing.csv', index=False)


#merge_cen_cr_bea_spatial()


def merge_cen_cr_bea_spatial_officers():
    cen_cr_bea_spatial = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial/Census_Crime_BEA_Spatial.csv')
    officers_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/officers/leoka_req_vars.csv')

    cen_cr_bea_spatial_officers_merged = cen_cr_bea_spatial.merge(officers_df, left_on=['ORI', 'YEAR'], right_on=['ori', 'year'], how='left')

    # Drop duplicate ori, agency, year columns from officers file
    cen_cr_bea_spatial_officers_merged.drop(['ori', 'agency', 'year'], axis=1, inplace=True)
    cen_cr_bea_spatial_officers_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial_officers/Census_Crime_BEA_Spatial_Officers.csv', index=False)

#merge_cen_cr_bea_spatial_officers()


def merge_cen_cr_bea_spatial_officers_arrests():
    cen_cr_bea_spatial_officers = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial_officers/Census_Crime_BEA_Spatial_Officers.csv')
    arrests_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/arrests/Arrests_Req_Vars_Indexes.csv')
    cen_cr_bea_spatial_officers_merged = cen_cr_bea_spatial_officers.merge(arrests_df, left_on=['ORI', 'YEAR'], right_on=['ori', 'year'], how='left')

    cen_cr_bea_spatial_officers_merged.drop(['ori', 'year'], axis=1, inplace=True)
    cen_cr_bea_spatial_officers_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial_officers_arrests/Census_Crime_BEA_Spatial_Officers_Arrests.csv', index=False)


#merge_cen_cr_bea_spatial_officers_arrests()


def merge_cen_cr_bea_spatial_officers_arrests_incarceration():
    cen_cr_bea_spatial_officers_arrests = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial_officers_arrests/Census_Crime_BEA_Spatial_Officers_Arrests.csv')
    incarc_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/incarceration/incarc_req_vars.csv')

    cen_cr_bea_spatial_officers_arrests_incarc_merged = cen_cr_bea_spatial_officers_arrests.merge(incarc_df, left_on=['STATEFP', 'CNTY', 'YEAR'], right_on=['STATEFP', 'CNTY', 'year'], how='left')

    cen_cr_bea_spatial_officers_arrests_incarc_merged['state'] = cen_cr_bea_spatial_officers_arrests_incarc_merged['state_x']
    cen_cr_bea_spatial_officers_arrests_incarc_merged.drop(['state_x', 'state_y', 'year'], axis=1, inplace=True)
    cen_cr_bea_spatial_officers_arrests_incarc_merged.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/census_crime_bea_spatial_officers_arrests_incarceration/Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration.csv', index=False)


#merge_cen_cr_bea_spatial_officers_arrests_incarceration()


"""
    Merge or concatenate these new columns with the final_main_race_rates df based on state and cnty fips so that for a given cnty and state combination, 
    same values are copied to all the jurisdictions.
"""


def merge_final_main_race_rates_incarceration_pct():
    # Read the cnty crime totals file
    cnty_agency_totals_98_08 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/agency_crime_totals_98_08.csv')
    cnty_agency_totals_98_08 = cnty_agency_totals_98_08[['ORI', 'perc_felonies', 'perc_misdemeanors']]
    # Read the final main rates arce file
    final_main_race_rates = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates_race_counts.csv')

    # # inner merge to have only the matching records i.e to
    # # retain only those agencies that have data for atleast 1 year between 1998-2008
    # # so each agency under a given county has the corresponding incarc pcts
    # final_main_race_rates_crime_totals = final_main_race_rates.merge(cnty_crime_totals_98_08, on=['STATEFP', 'CNTY'])
    #
    #
    # # ############# To-Do: To combine the below 2 operations into one #################
    # # # final_main_race_rates_crime_totals_prsn_clnd = final_main_race_rates_crime_totals.query('tot_cnty_prisons_pct != 0')
    # # # final_main_race_rates_crime_totals_jail_clnd = final_main_race_rates_crime_totals_prsn_clnd.query('tot_cnty_jails_pct != 0')
    # #
    #
    # # Create agency level crime totaks
    # final_main_race_rates_crime_totals['tot_felonies_agency'] = final_main_race_rates_crime_totals[['murder', 'manslaughter', 'rape', 'robbery', 'aggravated_assault', 'burglary', 'auto_theft']].sum(axis=1)
    # final_main_race_rates_crime_totals['tot_misdemeanors_agency'] = final_main_race_rates_crime_totals[['larceny', 'simple_assault']].sum(axis=1)
    # final_main_race_rates_crime_totals['tot_major_offenses_agency'] = final_main_race_rates_crime_totals[['tot_felonies_agency', 'tot_misdemeanors_agency']].sum(axis=1)
    #
    # # calculate incarceration percentages for each agency
    # final_main_race_rates_crime_totals['incarc_prison_perc'] = (final_main_race_rates_crime_totals['tot_felonies_agency']/final_main_race_rates_crime_totals['tot_felonies_cnty'])* 100
    # final_main_race_rates_crime_totals['incarc_jail_perc'] = (final_main_race_rates_crime_totals['tot_misdemeanors_agency']/final_main_race_rates_crime_totals['tot_misdemeanors_cnty']) * 100
    # final_main_race_rates_crime_totals['incarc_perc'] = (final_main_race_rates_crime_totals['tot_major_offenses_agency']/final_main_race_rates_crime_totals['tot_major_offenses_cnty']) * 100
    #
    # cnty_crime_totals_98_08 = None
    # final_main_race_rates = None

    final_main_race_rates_crime_totals = final_main_race_rates.merge(cnty_agency_totals_98_08, on = ['ORI'])
    final_main_race_rates_crime_totals.replace(np.inf, 0, inplace=True)
    final_main_race_rates_crime_totals.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates_race_counts_incarc_pct.csv',index=False)



merge_final_main_race_rates_incarceration_pct()