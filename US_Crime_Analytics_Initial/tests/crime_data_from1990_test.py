import pandas as pd

crime_data = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/tests/test_data_files/crime_data_from1990_test.csv')

print('Initital: ', crime_data)
crime_data_from_1990 = crime_data[crime_data.year >= 1990]

print()
# print(crime_data_from_1990.columns.tolist())

print(crime_data[1:])

