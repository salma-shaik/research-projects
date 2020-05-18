import pandas as pd

def df_combine_first(file1, file2, f_type):  
    if f_type == 'csv':
        old_data = pd.read_csv(file1, encoding = "ISO-8859-1")
        new_data = pd.read_csv(file2, encoding = "ISO-8859-1")
    elif f_type == 'excel':
        old_data = pd.read_excel(file1, encoding = "ISO-8859-1")
        new_data = pd.read_excel(file2, encoding = "ISO-8859-1")
    else:
        return 'Invalid file type'
    
    old_df = pd.DataFrame(old_data)
    new_df = pd.DataFrame(new_data)

    combined_df = new_df.combine_first(old_df)   
    print(combined_df)

df_combine_first('projects/test_data_files/combine_first_old.xlsx', 'projects/test_data_files/combine_first_new.xlsx', 'excel')

"""
INPUT:
old df:
   Employee_ID first_name  salary     skills
0            1       John    2000        C++
1            2       Mary    1500       Java
2            3        Sam    3000     Python
3            5       Anne    3500  Scripting
4            6      Maria    1500    Testing

new df:
   Employee_ID  age last_name  salary  skills
0            1   34       Doe    2000    Perl
1            2   23     Smith    5500    Java
2            3   56     Jacob    3500  Python
3            4   25     Clark    2000   Excel

OUTPUT:
   Employee_ID   age first_name last_name  salary   skills
0          1.0  34.0       John       Doe  2000.0     Perl
1          2.0  23.0       Mary     Smith  5500.0     Java
2          3.0  56.0        Sam     Jacob  3500.0   Python
3          4.0  25.0       Anne     Clark  2000.0    Excel
4          6.0   NaN      Maria       NaN  1500.0  Testing

"""
