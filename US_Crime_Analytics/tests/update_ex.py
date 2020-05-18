import pandas as pd

def df_update(file1, file2):  
    old_data = pd.read_csv(file1, encoding = "ISO-8859-1")
    old_df = pd.DataFrame(old_data)
   
    #new_data = pd.read_csv(file2, encoding = "ISO-8859-1")
    new_data = pd.read_excel(file2, encoding = "ISO-8859-1")
    new_df = pd.DataFrame(new_data)
    
    old_df.update(new_df)
    print(old_df,'\n')
    print(old_df.dtypes)

# update old df with new
# df_update('projects/test_data_files/update_old.csv', 'projects/test_data_files/update_new.csv')

"""
INPUT:

old df:
   emp_id first_name  salary  skills
0       1       John    2000     C++
1       2       Mary    1500    Java
2       3        Sam    3000  Python
3       4       Anne    3800     PHP 

new_df:
   emp_id last_name  salary    skills
0       1       Doe    4000      Perl
1       2     Smith    5500      Java
2       3     Jacob    2500       SQL
3       5     Clark    4200   Testing
4       6      Dave    3700  Scipting 

OUTPUT:
   emp_id first_name  salary   skills
0       1       John    4000     Perl
1       2       Mary    5500     Java
2       3        Sam    2500      SQL
3       5       Anne    4200  Testing 

dtypes:
emp_id         int64
first_name    object
salary         int64
skills        object
dtype: object

"""

# update old df with new df which has a string value under salary column
df_update('projects/test_data_files/update_old.csv', 'projects/test_data_files/update_new_text_sal.xlsx')

"""
INPUT:

old df:
   emp_id first_name  salary  skills
0       1       John    2000     C++
1       2       Mary    1500    Java
2       3        Sam    3000  Python
3       4       Anne    3800     PHP 

new_df:
   emp_id last_name  salary skills
0       1       Doe    2000   Perl
1       2     Smith  $5,500   Java
2       3     Jacob    2500    SQL 

OUTPUT:
   emp_id first_name  salary skills
0     1.0       John    2000   Perl
1     2.0       Mary  $5,500   Java
2     3.0        Sam    2500    SQL
3     4.0       Anne    3800    PHP 

dtypes:
emp_id        float64
first_name     object
salary         object
skills         object
dtype: object


A column with mixed dtypes is converted to a generic 'object' dtype that can hold any python object. 
Hence the dtype of the updated salary column is converted to an 'object' dtype
"""




