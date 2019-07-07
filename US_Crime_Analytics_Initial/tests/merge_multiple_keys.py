import pandas as pd

df_old = pd.read_excel("test_data_files/merge_ex1_old.xlsx", encoding = "ISO-8859-1")

df_new = pd.read_excel("test_data_files/merge_ex1_new.xlsx", encoding = "ISO-8859-1")

merged_df = pd.merge(df_old, df_new, on=['emp_id', 'state_id'])
print(merged_df)
