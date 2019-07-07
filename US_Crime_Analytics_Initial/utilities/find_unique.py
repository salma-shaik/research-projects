import pandas as pd
#
# """
# # Finding Id2 from DEC_10_SF1_P12_with_ann.csv that don't have a matching STCO_FIPS in Final_Main_Var_1990_2001.csv file
# main_file_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/Final_Main_Var_1990_2001.csv')
# main_file_stco_fips_set = set(main_file_df['STCO_FIPS'])
# print(main_file_stco_fips_set.__len__())
#
# county_census_2010_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann.csv', encoding = "ISO-8859-1")
# county_census_2010_df_id2_set = set(county_census_2010_df['GEO.id2'])
#
# print(county_census_2010_df_id2_set.__len__())
# print((county_census_2010_df_id2_set-main_file_stco_fips_set).__len__())
# """
#
#
# final_crime_for_merge_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_crime_for_merge.csv')
#
# print('final_crime_for_merge_df ', set(final_crime_for_merge_df['ORI']).__len__())
#
# final_main = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main.csv')
# print('final_main: ', set(final_main['ORI']).__len__())
# print('final_main placename missing: ', final_main[final_main.placename == 'Missing'].shape[0])

#
#
# Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration.csv')
# print('Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration ', set(Census_Crime_BEA_Spatial_Officers_Arrests_Incarceration['ORI']).__len__())
#
# Census_Interpolated = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/interpolated_files/Census_Interpolated.csv')
# print('Census_Interpolated ', set(Census_Interpolated['ORI']).__len__())
#
# crime_98_08_tot_non_zero = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_98_08_tot_non_zero.csv')
# print('crime_98_08_tot_non_zero ', set(crime_98_08_tot_non_zero['ORI']).__len__())
#
#
# crime_98_08_tot_zero = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_98_08_tot_zero.csv')
# print('crime_98_08_tot_zero ', set(crime_98_08_tot_zero['ORI']).__len__())
#
# #crime_zero_non_zero = crime_98_08_tot_non_zero['ORI'].intersection(crime_98_08_tot_zero['ORI'])
# #
# # print('crime_zero_non_zero: ', crime_zero_non_zero.shape[0])
#
# crime_98_08_tot = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_98_08_tot.csv')
# print('crime_98_08_tot: ', set(crime_98_08_tot['ORI']).__len__())
#

# final_main_race_rates_incarc_pct = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_race_rates_incarc_pct.csv')
# #print('final_main_race_rates_incarc_pct: ', set(final_main_race_rates_incarc_pct['ORI']).__len__())
#
# # print(final_main_race_rates_incarc_pct.head())
# print('final_main_race_rates_incarc_pct counties: ', set(final_main_race_rates_incarc_pct[final_main_race_rates_incarc_pct.Govt_level==1]['ORI']).__len__())

# Get the ORIs which are different between crime_non_zero_totals and crime_req_yrs_cnty_totals_groupby. These ORIs should be at county level and difference should show what's missing
#
# crime_non_zero_totals_uniq = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_cnty_98_08_totals_pcts.csv')
# crime_non_zero_totals_uniq['st_cnty_fips'] = crime_non_zero_totals_uniq['STATEFP'] + crime_non_zero_totals_uniq['CNTY']
# print('crime_non_zero_totals_uniq: ', set(crime_non_zero_totals_uniq['st_cnty_fips']).__len__())
#
# crime_req_yrs_cnty_totals_groupby_uniq = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/crime_req_yrs_cnty_totals_groupby.csv')
# crime_req_yrs_cnty_totals_groupby_uniq
# print('crime_req_yrs_cnty_totals_groupby_uniq: ', set(crime_req_yrs_cnty_totals_groupby_uniq['STATEFP', 'CNTY']).__len__())

# final_main_race_rates_incarc_pct = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_race_rates_incarc_pct.csv')
# print('final_main_race_rates_incarc_pct: ', set(final_main_race_rates_incarc_pct['ORI']).__len__())

final = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US Crime Analytics/data/crime/crime_with_updated_fbi_pop.csv')
print('final: ', set(final['ORI']).__len__())
