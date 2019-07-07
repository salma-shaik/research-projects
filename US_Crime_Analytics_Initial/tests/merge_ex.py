import pandas as pd

"""
KEY SPECIFIC:
'merge' - if we want to merge/combine data-frames based on a specific key and also to define specific type of join
By default, merge does an inner join and repeats the similar column with x and y suffixes.
"""

## EXAMPLE 1: old df has 4 employees and new df has only 3 employees
def df_merge(file1, file2, merge_type=None):  
    old_data = pd.read_excel(file1, encoding = "ISO-8859-1")
    old_df = pd.DataFrame(old_data)
    # print(old_df,'\n')
    new_data = pd.read_excel(file2, encoding = "ISO-8859-1")
    new_df = pd.DataFrame(new_data)
    # print(new_df,'\n')
	
    if merge_type == None:
        merged_df = pd.merge(old_df, new_df, on='emp_id') # inner join by default
    else:
        merged_df = pd.merge(old_df, new_df, on='emp_id', how="{}".format(merge_type))
        return merged_df
        
    print(merged_df)

# df_merge('projects/test_data_files/merge_ex1_old.xlsx', 'projects/test_data_files/merge_ex1_new.xlsx')

"""
INPUT:

old df:
   age  emp_id first_name  salary     skills
0   23       1       John    2000        C++
1   56       2       Mary    1500       Java
2   43       3        Sam    3000     Python
3   32       5        Ann    1800  Scripting 

new df:
   emp_id last_name  salary skills
0       1       Doe    4000   Perl
1       2     Smith    5500   Java
2       3     Jacob    2500    SQL 

OUTPUT:
   age  emp_id first_name  salary_x skills_x last_name  salary_y skills_y
0   23       1       John      2000      C++       Doe      4000     Perl
1   56       2       Mary      1500     Java     Smith      5500     Java
2   43       3        Sam      3000   Python     Jacob      2500      SQL


Fixed in the next cases
"""

# Outer join to get all the data from both the data-frames
merged_df = df_merge('projects/test_data_files/merge_ex1_old.xlsx', 'projects/test_data_files/merge_ex1_new.xlsx', 'outer')
print(merged_df, '\n')

"""
INPUT:

old df:
   age  emp_id first_name  salary     skills
0   23       1       John    2000        C++
1   56       2       Mary    1500       Java
2   43       3        Sam    3000     Python
3   32       5        Ann    1800  Scripting 

new df:
   emp_id last_name  salary skills
0       1       Doe    4000   Perl
1       2     Smith    5500   Java
2       3     Jacob    2500    SQL 

OUTPUT:
   age  emp_id first_name  salary_x   skills_x last_name  salary_y skills_y
0   23       1       John      2000        C++       Doe    4000.0     Perl
1   56       2       Mary      1500       Java     Smith    5500.0     Java
2   43       3        Sam      3000     Python     Jacob    2500.0      SQL
3   32       5        Ann      1800  Scripting       NaN       NaN      NaN

"""

# This can be fixed as below

def clean_df(df):
    # Creating salary and skills columns by replacing NaNs in _y columns with corresponding values from _x columns
    #then drop the _x and _y columns
    merged_df['salary'] = merged_df['salary_y'].fillna(merged_df['salary_x'])
    merged_df['skills'] = merged_df['skills_y'].fillna(merged_df['skills_x'])
    print(merged_df.drop(['salary_x', 'salary_y', 'skills_x', 'skills_y'], axis=1))

clean_df(merged_df)

"""
OUTPUT:

   age  emp_id first_name last_name  salary     skills
0   23       1       John       Doe  4000.0       Perl
1   56       2       Mary     Smith  5500.0       Java
2   43       3        Sam     Jacob  2500.0        SQL
3   32       5        Ann       NaN  1800.0  Scripting

"""

## EXAMPLE 2:  If an emp_id cell has no value
merged_df = df_merge('projects/test_data_files/merge_ex1_old.xlsx' 'projects/test_data_files/merge_ex1_new_missing_empid.xlsx', 'outer')
clean_df(merged_df)

"""
INPUT:
old df:

   age  emp_id first_name  salary     skills
0   23       1       John    2000        C++
1   56       2       Mary    1500       Java
2   43       3        Sam    3000     Python
3   32       5        Ann    1800  Scripting 

new df:
   emp_id last_name  salary skills
0     1.0       Doe    4000   Perl
1     NaN     Smith    5500   Java
2     3.0     Jacob    2500    SQL 


OUTPUT:
    age  emp_id first_name last_name  salary     skills
0  23.0     1.0       John       Doe  4000.0       Perl
1  56.0     2.0       Mary       NaN  1500.0       Java
2  43.0     3.0        Sam     Jacob  2500.0        SQL
3  32.0     5.0        Ann       NaN  1800.0  Scripting
4   NaN     NaN        NaN     Smith  5500.0       Java

"""


# EXAMPLE 3: Another example
merged_df = df_merge('projects/test_data_files/merge_ex2_old.xlsx', 'projects/test_data_files/merge_ex2_new.xlsx', 'outer')
clean_df(merged_df)
"""
OUTPUT:
    emp_id first_name last_name   age  salary                 skills
0        1       John       NaN   NaN  2000.0                    C++
1        2       Mary       NaN   NaN  1500.0                   Java
2        3        Sam       NaN   NaN  3000.0                 Python
3        4        Ann       Doe  23.0  4000.0                   Perl
4        5     Rachel     Smith  56.0  5500.0                   Java
5        6      Karen     Jacob  43.0  4500.0          [Python, SQL]
6        7      Scott    Taylor  32.0  1800.0                Testing
7        8      James       NaN   NaN  5200.0                   Math
8        9       Nick     Evans  24.0  4300.0  [AutoCAD, SolidWorks]
9       10      Jason       NaN   NaN  4920.0                    Art
10      11        NaN      Wood  34.0  3400.0                    PHP
11      12        NaN   Michael  28.0  5600.0              Languages

"""