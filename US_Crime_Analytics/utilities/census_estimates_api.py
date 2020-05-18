import pandas as pd
import requests
import json
import csv
import time
import datetime

#
# def get_census_estimates_data_from_api(base_url, fips_df, op_file, census_year=None):
#     """
#     :param base_url: Different base url for 2000 and 2010 years
#     :param fips_df: df with state and county fips codes
#     :param op_file: op file name to which the census data needs to be written
#     :param census_year: year for which decennial census data
#     :return:
#     """
#     # take a count variable to help distinguish 1st request from subsequent requests so that we take the variable
#     # names only from the 1st call as the header names and skip varibale names from the subsequent calls.
#     count = 0
#     # open a new file with the required output file name
#     with open(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/{op_file}.csv', 'w') as file_wrtr:
#         # take a csv writer object to write to this output file
#         op_file_writer = csv.writer(file_wrtr)
#
#         # Iterate over each row in the state_county fips df
#         for row in fips_df.itertuples():
#             # create the rquest url for ecah state and fips code to get the data for all county subdivisions under it
#             try:
#                 print('count: ', count)
#
#                 """ Use timer if needed """
#                 # if count in [500, 1000, 1500, 2000, 2500, 3000]:
#                 #     time.sleep(3600)
#
#                 st_fips = str(getattr(row, "state"))
#                 cnty_fips = str(getattr(row, "county"))
#
#                 if census_year == 2010:
#                     # for 2010, state and county fips need to of size 2 and 3 respectively. Hence prepend with zeroes as required
#                     if st_fips.__len__() < 2:
#                         st_fips = '0' + st_fips
#
#                     if cnty_fips.__len__() < 3:
#                         cnty_fips = ('0'*(3-cnty_fips.__len__())) + cnty_fips
#
#                 response = requests.get(f'{base_url}?get=NAME,P012001,P012A001,P012B001,P012H001,P012A006,P012A007,P012A008,P012A009,P012A010,P012A002,P012A030,P012A031,P012A032,P012A033,P012A034,P012A026,P012B006,P012B007,P012B008,P012B009,P012B010,P012B002,P012B030,P012B031,P012B032,P012B033,P012B034,P012B026,P012H002,P012H006,P012H007,P012H008,P012H009,P012H010,P012H030,P012H031,P012H032,P012H033,P012H034,P012H026&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72')
#
#                 # load the json in to python object which would be list of all entries in the json object
#                 resp = json.loads(response.content)
#                 # If this is the first call(count=0), then write the entire content so that the 1st row with the variable names is the header
#                 if count == 0:
#                     # iterate over respone python object and write each row to the csv
#                     for res in resp:
#                         op_file_writer.writerow(res)
#                 else:
#                     # skipping 1st row which are the variable names starting from 2nd calls.
#                     for res in resp[1:]:
#                         op_file_writer.writerow(res)
#
#                 count += 1
#
#             except Exception as ex:
#                 print('Error code: ', response.status_code)
#                 print('Error Response: ', response.content)
#                 print('Exception: ', ex)
#                 print('Total API Calls: ', count)
#                 break
#
#
# # Get 2000 township census data
# # st_cnty_fips_00 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/st_cnty_fips_2000.csv')
# # get_census_data_from_api('https://api.census.gov/data/2000/sf1', st_cnty_fips_00, 'new_census_townships_00_initial') # 3141 calls
#
# # Get 2010 township census data
# st_cnty_fips_10 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/st_cnty_fips_10_temp.csv')
#
# get_census_estimates_data_from_api('https://api.census.gov/data/2010/dec/sf1', st_cnty_fips_10, 'new_census_townships_10_initial_16th', 2010)


def get_estimates(api_url, op_file):
    # open a new file with the required output file name
    with open(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/estimates/test/{op_file}.csv', 'w') as file_wrtr:
        # take a csv writer object to write to this output file
        op_file_writer = csv.writer(file_wrtr)

        response = requests.get(api_url)
        resp = json.loads(response.content)

        # iterate over respone python object and write each row to the csv
        for res in resp:
            op_file_writer.writerow(res)

# acs api (2010-2017)
# B00001_001E	Estimate!!Total	UNWEIGHTED SAMPLE COUNT OF THE POPULATION
#get_estimates('https://api.census.gov/data/2011/acs/acs5?get=B01001_001E,NAME&for=county:*&in=state:26&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72', 'acs_mi_cnts_11')

# 2000-2010
get_estimates('https://api.census.gov/data/2009/pep/int_charagegroups?get=AGEGROUP,RACE,SEX,DATE_DESC,HISP,POP&for=county:*&in=state:26&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72', 'acs_mi_cnts_09')

#pep api (2010-2017)
get_estimates('https://api.census.gov/data/2011/pep/charagegroups?get=POP,GEONAME&for=county:*&in=state:26&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72', 'pep_mi_cnts_11')


def check_acs_pep_pop():
    acs_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/estimates/test/acs_mi_cnts_11.csv')
    pep_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/estimates/test/pep_mi_cnts_11.csv')

    acs_pep_mi_cnty = pd.concat([acs_df, pep_df], axis=1)

    acs_pep_mi_cnty['pop_diff'] = acs_pep_mi_cnty['POP']-acs_pep_mi_cnty['B01001_001E']

    acs_pep_mi_cnty.sort_values(by=['pop_diff'], inplace=True)
    acs_pep_mi_cnty.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/estimates/test/acs_pep_mi_cnty_popdiff_11.csv', index=False)

check_acs_pep_pop()