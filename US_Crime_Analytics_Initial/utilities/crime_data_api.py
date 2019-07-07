import pandas as pd

import pandas as pd
import requests
import json
import csv


def get_crime_data(api_url, op_file):
    # open a new file with the required output file name
    with open(f'/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/crime_data/{op_file}.csv', 'w') as file_wrtr:
        # take a csv writer object to write to this output file
        response = requests.get(api_url)
        resp = json.loads(response.content)
        crime_data = resp['results']

        # iterate over respone python object and write each row to the csv
        # for res in resp['results']:
        #     op_file_writer.writerow(res.values)
        keys = crime_data[0].keys()
        op_file_writer = csv.DictWriter(file_wrtr, keys)
        op_file_writer.writeheader()
        op_file_writer.writerows(crime_data)

get_crime_data('https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/MI8218200/offenses/1995/2017?api_key=1MMO3GOYhSL8nhnZzZW0lmfPJYrcDH76YWC5Q7mA', 'crime_data_MI82182')