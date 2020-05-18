import pandas as pd

""""
Ginni's test - Stack year wise columns side by side
"""


"""
Function to update the column headers by corresponding year.
"""


def update_col_headers(df, year):
    df_cols = df.columns.tolist()
    df_cols_updated = []
    for col in df_cols:
        col = col + '_' + year
        df_cols_updated.append(col)
    return df_cols_updated

"""
Execution starts from here
"""
df_2013 = pd.read_excel('/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/ginni_2013.xlsx')
df_2013 = df_2013.drop(['YEAR'], axis=1)
df_2013.columns = update_col_headers(df_2013, '2013')

df_2014 = pd.read_excel('/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/ginni_2014.xlsx')
df_2014 = df_2014.drop(['AREA_NEW', 'YEAR'], axis=1)
df_2014.columns = update_col_headers(df_2014, '2014')

df_2015 = pd.read_excel('/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/ginni_2015.xlsx')
df_2015 = df_2015.drop(['AREA_NEW', 'YEAR'], axis=1)
df_2015.columns = update_col_headers(df_2015, '2015')

df_2016 = pd.read_excel('/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/ginni_2014.xlsx')
df_2016 = df_2016.drop(['AREA_NEW', 'YEAR'], axis=1)
df_2016.columns = update_col_headers(df_2016, '2016')

## concatenate all the dataframes side by side
final_df = pd.concat([df_2013, df_2014, df_2015, df_2016], axis=1)

print(final_df.head())

## Write final df to an excel. Change it to the required location on your system
final_df.to_excel('/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/tests/test_data_files/ginni_final.xlsx', index=False)
