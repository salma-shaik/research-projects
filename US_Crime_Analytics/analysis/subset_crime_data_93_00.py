import pandas as pd


def get_final_main_90_00_15():
    final_main = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/Census_Crime_BEA_Spatial.csv')
    years = [1990, 2000, 2015]
    final_main_subset = final_main[final_main.YEAR.isin(years)]
    final_main_subset.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/Census_Crime_BEA_Spatial_Merged_90_00_15.csv', index=False)

get_final_main_90_00_15()


def get_final_main_min_crime_93_00():
    final_main = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/Census_Crime_BEA_Spatial.csv')

    final_main_subset = {ORI: crime_year.tolist() for ORI, crime_year in final_main.groupby('ORI')['crime_year']}
    final_main_subset_df = pd.DataFrame(final_main_subset)
    final_main_subset_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/ORIs_Crime_Years.csv', index=False)

    req_yrs =  [1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]

    req_ori = []

    # for col in final_main_subset_df.columns.tolist():
    for key, value in final_main_subset.items():
        if all(elem in value for elem in req_yrs):
            req_ori.append(key)

    final_main_min_90_13 = final_main_subset_df[req_ori]

    final_main_min_90_13.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/ORIs_Crime_Min_93-00.csv', index=False)

    # Then subset the data to get only those ORI records from final main file which are in the ORIs_Crime_Min_93-00.csv
    final_main_crime_min_90_00_ori = final_main[final_main.ORI.isin(req_ori)]

    final_main_crime_min_90_00_ori.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/Census_Crime_BEA_Spatial_Crime_Min_93-00.csv', index=False)


    # Then subset data to have records for only years 1993 to 2000
 
    """
        ################ TO-DO: check if this needs to be handled ############# 
        UserWarning: Boolean Series key will be reindexed to match DataFrame index.
        final_main_subset_90_00_only = final_main_crime_min_90_00_ori[final_main.YEAR.isin(years)]
    """
    final_main_subset_93_00_only = final_main_crime_min_90_00_ori[final_main.YEAR.isin(req_yrs)]
    final_main_subset_93_00_only.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data/analysis/Census_Crime_BEA_Spatial_Crime_93-00_Only.csv', index=False)

get_final_main_min_crime_93_00()