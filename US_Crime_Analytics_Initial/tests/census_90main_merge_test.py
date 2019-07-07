import pandas as pd
#
#
# def get_fips_ori_agency_90final(file_path):
#     final_main_df = pd.read_csv(file_path)
#     final_main_fips_ori_agency = final_main_df[['ORI', 'AGENCY', 'CGOVTYPE', 'FIPS_STATE', 'FIPS_PLACE']]
#
#     print()
#     """
#     1. Obtain only unique records from the final main file - key: fips place + fips state
#     """
#     final_main_fips_ori_agency_unique = final_main_fips_ori_agency.drop_duplicates(['FIPS_STATE', 'FIPS_PLACE']) # --> 11,602 rows
#
#     """
#     2. Rename CGOVTYPE, FIPS_STATE, FIPS_PLACE to Govt_level, 'STATEFP', 'place_fips' to match national census file
#     """
#     final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.rename(
#         {'CGOVTYPE': 'Govt_level', 'FIPS_STATE': 'STATEFP', 'FIPS_PLACE': 'place_fips'}, axis='columns')
#
#     """
#     3. Get only those records from 90 final main file whose cgovtype is 1,2 or 3
#     """
#     final_main_fips_ori_agency_unique = final_main_fips_ori_agency_unique.loc[
#         final_main_fips_ori_agency_unique['Govt_level'].isin([1, 2, 3])]
#
#     # final_main_fips_ori_agency_unique.to_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/wip_merge_files/final_main_fips_ori_agency_unique.csv', index=False)
#
#     return final_main_fips_ori_agency_unique
#
#
# final_uniqe_90main_df = get_fips_ori_agency_90final('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/wip_merge_files/Final_Main_Var_1990_2001.csv')
# final_uniqe_90main_df_cols = set(final_uniqe_90main_df.columns.tolist())
# # reqd_final_df = pd.read_csv('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/wip_merge_files/final_main_fips_ori_agency_unique.csv')
#
# # govt_level = final_uniqe_90main_df['Govt_level']
# # print(govt_level.value_counts())
# """
# Govt_level
# 2               7617
# 1               2647
# 3               1336
# """
#
#
# # counties_file = 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2000/new_census_variables/new_vars_census_county_2000.csv'
# # cities_file = 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2000/new_census_variables/new_vars_census_cities_2000.csv'
#
# counties_file = 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2010/new_census_variables/new_vars_census_county_2010.csv'
# cities_file = 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_cities_2010/new_census_variables/new_vars_census_cities_2010.csv'
#
# cnty_df = pd.read_csv(counties_file)
#
# cities_df = pd.read_csv(cities_file)
# national_census_df = cnty_df.append([cities_df])
#
# """
# 2.
# Merge national all census files with 1990 final main file to get the correct cgovtype based on fips state, fips place.
# Also obtain ORI and Agency columns from final main file.
# Inner join coz we want only those agencies that are present in both the files so that we can analyze agencies that have data consistently over time
# """
# national_census_df = national_census_df.merge(final_uniqe_90main_df, on=['STATEFP', 'place_fips'])
#
# # Govt_level after merging
# print(national_census_df['Govt_level_y'].value_counts())


"""
MERGE TEST
"""
df1 = pd.DataFrame({'STATEFP': [1,2,3], 'place_fips': [11, 22, 33], 'ORI': [111, 222, 333], 'AGENCY': [1111, 2222, 3333], 'Govt_level': ['one', 'one-two', 'two-three']})
df2 = pd.DataFrame({'ORI': [333, 111, 555, 666, 222, 444], 'AGENCY': [1111, 2222, 45435, 6456546, 3333, 4444], 'STATEFP': [1,12,3, 546, 645, 4], 'place_fips': [11, 22, 33,67, 56, 44], 'Govt_level': ['one', 'two', 'three', 'three', 'rtyrt', 'rtytry'], 'Pct_WYM': ['oneone', 'twotwo', 'threethree', 'fourfour', 'rtytr', 'retrety'], 'Pct_WYF': ['fone', 'twotwo', 'fthree', 'ffour', 'ryrty', 'rtyrty']})

# merged_df2 = df2.merge(df1, on=['STATEFP', 'place_fips'], suffixes=('_2000', '_90final'))
#
# print(merged_df2)

ori = [222, 333]

df2_r = df2[df2.ORI.isin(ori)]

print(df2_r)