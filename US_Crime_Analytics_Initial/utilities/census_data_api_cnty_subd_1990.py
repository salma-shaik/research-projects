import pandas as pd
import requests
import json
import csv
import os


def get_census_data_from_api(base_url, fips_df, op_file):
    count = 0

    with open(
            f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/census_cities_1990/{op_file}.csv',
            'w') as file_wrtr:
        # take a csv writer object to write to this output file
        op_file_writer = csv.writer(file_wrtr)

        for row in fips_df.itertuples():
            try:
                print('count: ', count)
                st_fips = str(getattr(row, "state"))
                cnty_fips = str(getattr(row, "county"))

                if st_fips.__len__() < 2:
                    st_fips = '0' + st_fips

                if cnty_fips.__len__() < 3:
                    cnty_fips = ('0' * (3 - cnty_fips.__len__())) + cnty_fips

                response = requests.get(
                    f'{base_url}?get=NAME,P012001,P012A001,P012B001,P012H001,P012A006,P012A007,P012A008,P012A009,P012A010,P012A002,P012A030,P012A031,P012A032,P012A033,P012A034,P012A026,P012B006,P012B007,P012B008,P012B009,P012B010,P012B002,P012B030,P012B031,P012B032,P012B033,P012B034,P012B026,P012H002,P012H006,P012H007,P012H008,P012H009,P012H010,P012H030,P012H031,P012H032,P012H033,P012H034,P012H026&for=county%20subdivision:*&in=state:{st_fips}%20county:{cnty_fips}&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72')

                resp = json.loads(response.content)

                if count == 0:
                    # iterate over respone python object and write each row to the csv
                    for res in resp:
                        op_file_writer.writerow(res)
                else:
                    # skipping 1st row which are the variable names starting from 2nd calls.
                    for res in resp[1:]:
                        op_file_writer.writerow(res)

                count += 1

            except Exception as ex:
                print('Error code: ', response.status_code)
                print('Error Response: ', response.content)
                print('Exception: ', ex)
                print('Total API Calls: ', count)
                break


# Get 1990 state and county fips
st_cnty_fips_90 = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/wip_merge_files/st_cnty_fips_1990.csv')

get_census_data_from_api('https://api.census.gov/data/2000/sf1', st_cnty_fips_90, 'new_census_townships_00_initial')