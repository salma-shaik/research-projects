import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import pandas as pd


def basic_crime_counts_by_year(yrs_range, var_type, x_label, y_label):

    final_main = pd.DataFrame()

    if yrs_range == '93-00':
        final_main = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/Census_Crime_BEA_Spatial_Crime_93-00_Only.csv')
    elif yrs_range == 'all':
        final_main = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates.csv')

    # total crime trend by year
    var_agg_year = final_main.groupby('YEAR')[var_type].sum()
    print()
    # total_crime.plot.bar()
    #total_crime.plot()
    plt.plot(var_agg_year)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

    """
        YEAR        
        1993    770287.0
        1994    420331.0
        1995    392005.0
        1996    353373.0
        1997    341930.0
        1998    306500.0
        1999    283577.0
        2000    286255.0
    """



# basic_crime_counts_by_year(yrs_range='93-00', var_type='total_crime', x_label='Year', y_label='Total Crime Counts')
# basic_crime_counts_by_year(yrs_range='93-00', var_type='violent_crime', x_label='Year', y_label='Violent Crime Count')
basic_crime_counts_by_year(yrs_range='93-00', var_type='property_crime', x_label='Year', y_label='Property Crime Count')


"""
final_main.groupby('YEAR')[var_type].max()
# property crime trend by year
pro_crime = final_main.groupby('YEAR')['property_crime'].sum()

# crimes against officers trend by year
crimes_agnst_officers = final_main.groupby('YEAR')['property_crime'].sum()

# robbery trend
# robbery_counts = final_main.groupby('YEAR')['robbery'].sum()

# violent crime trend by year
# vio_crime = final_main.groupby('YEAR')['violent_crime'].sum()
"""