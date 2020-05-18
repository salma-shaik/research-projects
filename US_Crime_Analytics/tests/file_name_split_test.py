import re

file_path = 'C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/census_county_2010/modified_files/DEC_10_SF1_P12_with_ann.csv'
file_name = file_path.split('/')[-1]
# print(file_name)
file_type = file_name.split('_')
print(file_type[3])
