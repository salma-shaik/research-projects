import pandas as pd

final_main = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates_race_counts_incarc_pct.csv')

final_main['prison_occupancy_count'] = (final_main['perc_felonies'] * final_main['total_prison_pop'])/100
final_main['jail_occupancy_count'] = (final_main['perc_misdemeanors'] * final_main['jail_interp'])/100

final_main.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates_race_counts_incarc_counts.csv', index=False)
