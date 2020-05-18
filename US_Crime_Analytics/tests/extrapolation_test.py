import pandas as pd
cen_test_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/tests/test_data_files/census_extrapolation_test.csv')
cen_test_df.sort_values(by=['ORI', 'YEAR'], ascending=[True, True], inplace=True)

# Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
cen_test_df = cen_test_df.reset_index(drop=True)

"""
    ORI	AGENCY	Govt_level	place_fips	placename	CNTY	STATEFP	YEAR	POP100	White_count	Black_count	Hispanic_count	Age1524_WhiteM	
    White_Males_All	Age1524_WhiteF	White_Females_All	Age1524_BlackM	Black_Males_All	Age1524_BlackF	Black_Females_All	Age1524_HispanicM	
    Hispanic_Males_All	Age1524_HispanicF	Hispanic_Females_All	Pct_WYM	Pct_WYF
"""

""" 
#####################
Tried to write a function but no way that we can pass variable to df. .. Need to give the actual column name 
def calculate_2015_pop_vars(df_row, pop_var):
    req_var = f'df_row.{pop_var} + (5 * (df_row.{pop_var} - cen_test_df.iloc[df_row.Index - 1].{pop_var}) / 10)'
    return int(req_var)
####################
"""


for row in cen_test_df.itertuples():
    if row.YEAR == 2010:
        """
        Creates a new dataframe by selecting or calculating required values for all the columns
        ORI	AGENCY	Govt_level	place_fips	placename	CNTY	STATEFP - values from 2010
        YEAR - 2015
        POP100 .... Pct_WYF - calculated as below
            value for 2010 + (5*(value for 2010 - value for 2000)/10)
            i.e averaging out the difference between 2010 and 2000 values and multiplying it 5 times to account for linear increase for 5 years from 2010
            
            row - has access to current row in the iteration
            cen_test_df.iloc[row.Index-1] - gives access to the previous row in the dataframe i.e 2000 row
            
            Not using round for Pct_WYM	Pct_WYF since they are proportions and will be < 1.
            
        """
        new_df = pd.DataFrame(
            {'ORI':
                 [row.ORI],
             'AGENCY':
                 [row.AGENCY],
             'Govt_level':
                 [row.Govt_level],
             'place_fips':
                 [row.place_fips],
             'placename':
                 [row.placename],
             'CNTY':
                 [row.CNTY],
             'STATEFP':
                 [row.STATEFP],
             'YEAR':
                 [2015],
             'POP100':
                 [round(row.POP100 + (5 * (row.POP100 - cen_test_df.iloc[row.Index-1].POP100)/10))],
             'White_count':
                 [round(row.White_count + (5 * (row.White_count - cen_test_df.iloc[row.Index - 1].White_count) / 10))],
             'Black_count':
                 [round(row.Black_count + (5 * (row.Black_count - cen_test_df.iloc[row.Index - 1].Black_count) / 10))],
             'Hispanic_count':
                 [round(row.Hispanic_count + (5 * (row.Hispanic_count - cen_test_df.iloc[row.Index - 1].Hispanic_count) / 10))],
             'Age1524_WhiteM':
                 [round(row.Age1524_WhiteM + (5 * (row.Age1524_WhiteM - cen_test_df.iloc[row.Index - 1].Age1524_WhiteM) / 10))],
             'White_Males_All':
                 [round(row.White_Males_All + (5 * (row.White_Males_All - cen_test_df.iloc[row.Index - 1].White_Males_All) / 10))],
             'Age1524_WhiteF':
                 [round(row.Age1524_WhiteF + (5 * (row.Age1524_WhiteF - cen_test_df.iloc[row.Index - 1].Age1524_WhiteF) / 10))],
             'White_Females_All':
                 [round(row.White_Females_All + (5 * (row.White_Females_All - cen_test_df.iloc[row.Index - 1].White_Females_All) / 10))],
             'Age1524_BlackM':
                 [round(row.Age1524_BlackM + (5 * (row.Age1524_BlackM - cen_test_df.iloc[row.Index - 1].Age1524_BlackM) / 10))],
             'Black_Males_All':
                 [round(row.Black_Males_All + (5 * (row.Black_Males_All - cen_test_df.iloc[row.Index - 1].Black_Males_All) / 10))],
             'Age1524_BlackF':
                 [round(row.Age1524_BlackF + (5 * (row.Age1524_BlackF - cen_test_df.iloc[row.Index - 1].Age1524_BlackF) / 10))],
             'Black_Females_All':
                 [round(row.Black_Females_All + (5 * (row.Black_Females_All - cen_test_df.iloc[row.Index - 1].Black_Females_All) / 10))],
             'Age1524_HispanicM':
                 [round(row.Age1524_HispanicM + (5 * (row.Age1524_HispanicM - cen_test_df.iloc[row.Index - 1].Age1524_HispanicM) / 10))],
             'Hispanic_Males_All':
                 [round(row.Hispanic_Males_All + (5 * (row.Hispanic_Males_All - cen_test_df.iloc[row.Index - 1].Hispanic_Males_All) / 10))],
             'Age1524_HispanicF':
                 [round(row.Age1524_HispanicF + (5 * (row.Age1524_HispanicF - cen_test_df.iloc[row.Index - 1].Age1524_HispanicF) / 10))],
             'Hispanic_Females_All':
                 [round(row.Hispanic_Females_All + (5 * (row.Hispanic_Females_All - cen_test_df.iloc[row.Index - 1].Hispanic_Females_All) / 10))],
             'Pct_WYM':
                 [row.Pct_WYM + (5 * (row.Pct_WYM - cen_test_df.iloc[row.Index - 1].Pct_WYM) / 10)],
             'Pct_WYF':
                 [row.Pct_WYF + (5 * (row.Pct_WYF - cen_test_df.iloc[row.Index - 1].Pct_WYF) / 10)]
          })
        # Append the new df with required column values for 2015 year
        cen_test_df = cen_test_df.append(new_df, ignore_index=True, sort=False)


"""
All the 2015 are rows are added at the bottom so need to sort again by ORI and YEAR to get the 3 occurences of each ORI together 
and then sort by YEAR(15,10,00,90)
"""
cen_test_df_sorted = cen_test_df.sort_values(by=['ORI', 'YEAR'], ascending=[True, False])

# Reset index after sorting so that it is in ascending order again and not trying to maintain the original index
cen_test_df_sorted = cen_test_df_sorted.reset_index(drop=True)