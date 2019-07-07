import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


final_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/analysis/final_main_rates.csv')


# Create weighted averages
def create_weighted_avgs(df, avg_name, weight_name):
    d = df[avg_name]
    w = df[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()


# Create graphs for trends
def graph_trends(trend_vars, title, xlbl, ylbl):
    for trend_var, pop_var in trend_vars.items():
        print(trend_var, ":", pop_var)
        plt_var = final_df.groupby("YEAR").apply(create_weighted_avgs, f'{trend_var}', f'{pop_var}')
        plt.plot(plt_var, label=f'{trend_var}')
        plt.legend()
        plt.title(f'{title}')
        plt.xlabel(f'{xlbl}')
        plt.ylabel(f'{ylbl}')
    plt.show()


"""
    1. Drug Arrests Trend By Race (Sale + Possession)
"""
# graph_trends({'drug_arrests_white_rate':'White_count', 'drug_arrests_black_rate':'Black_count'}, title='Drug Arrests Trend By Race', xlbl='Year', ylbl='Drug Arrests Rate')


"""
    2. Drug Sale Arrests Trend By Race
"""
# graph_trends({'sale_drug_total_tot_white_rate':'White_count', 'sale_drug_total_tot_black_rate':'Black_count'}, title='Drug Sale Arrests Trend By Race', xlbl='Year', ylbl='Drug Sale Arrests Rate')


"""
    3. Drug Possession Arrests Trend By Race
"""
# graph_trends({'poss_drug_total_tot_white_rate':'White_count', 'poss_drug_total_tot_black_rate':'Black_count'}, title='Drug Possession Arrests Trend By Race', xlbl='Year', ylbl='Drug Possession Arrests Rate')


"""
    4. Drug Possession Arrests Trend By Officers Rate
"""
# graph_trends({'poss_drug_total_tot_white_rate':'White_count', 'poss_drug_total_tot_black_rate':'Black_count'}, title='Drug Possession Arrests Trend By Race', xlbl='Year', ylbl='Drug Possession Arrests Rate')


"""
    5. Disorder Arrests Trend By Race
"""
# graph_trends({'disorder_arrests_white_index_rate':'White_count', 'disorder_arrests_black_index_rate':'Black_count'}, title='Disorder Arrests Trend By Race', xlbl='Year', ylbl='Disorder Arrests Rate')