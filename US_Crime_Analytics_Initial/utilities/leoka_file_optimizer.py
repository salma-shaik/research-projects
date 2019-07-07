import pandas as pd

leoka_df = pd.read_excel('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/officers/leoka_all_1990_2015.xlsx')

# get reqd cols
leoka_req = leoka_df[['ori', 'agency', 'year', 'total_officers']]

# write the df with req vars to file
leoka_req.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/officers/leoka_req_vars.csv', index=False)