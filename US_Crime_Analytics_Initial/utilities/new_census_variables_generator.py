import os
import shutil
import pandas as pd
import re
from utilities import clean_files as cf
from utilities import fips_codes_generator as fcg


def remove_revised_pop100(pop100_val, ptrn):
    pattern = re.compile(ptrn)
    match = pattern.search(pop100_val)
    if match:
        return pop100_val[:match.start()]
    else:
        return pop100_val


""" 
### Concise using indices
def create_new_census_cols(initial_df, new_df, pop_var, census_year=None, new_cen_vars=True):
    if new_cen_vars is False:
        # for 2010 city and 2010 county census files, total pop has revised number appended and it needs to be removed.
        new_df[f'{pop_var}'] = initial_df.iloc[:, 6]
        if census_year == '10':
            new_df[f'{pop_var}'] = new_df[f'{pop_var}'].apply(remove_revised_pop100, args=('\(',))
    else:
        new_df[f'{pop_var}_count'] = initial_df.iloc[:, 6]
        new_df[f'Age1524_{pop_var}M'] = initial_df.iloc[:, 11:16].sum(axis=1)
        new_df[f'{pop_var}_Males_All'] = initial_df.iloc[:, 7]
        new_df[f'Age1524_{pop_var}F'] = initial_df.iloc[:, 35:40].sum(axis=1)
        new_df[f'{pop_var}_Females_All'] = initial_df.iloc[:, 31]

        if pop_var == 'White':
            new_df['Pct_WYM'] = new_df['Age1524_WhiteM']/new_df['White_Males_All']
            new_df['Pct_WYF'] = new_df['Age1524_WhiteF'] / new_df['White_Females_All']

        return new_df
"""


def create_pop100_col(ini_df, new_df, census_year):
    if census_year == '00':
        new_df['POP100'] = ini_df.loc[:, 'P012VD01']
    if census_year == '10':
        # for 2010 city and 2010 county census files, total pop has revised number appended and it needs to be removed.
        new_df['POP100'] = ini_df.loc[:, 'P12D001']
        new_df['POP100'] = new_df['POP100'].apply(remove_revised_pop100, args=('\(',))
    return new_df


def create_white_cols(ini_df, new_df, census_year):
    if census_year == '00':
        new_df['White_count'] = ini_df.loc[:, 'P012AVD01']
        new_df['Age1524_WhiteM'] = ini_df.loc[:, ['P012AVD06', 'P012AVD07', 'P012AVD08', 'P012AVD09', 'P012AVD10']].sum(axis=1)
        new_df['White_Males_All'] = ini_df.loc[:, 'P012AVD02']
        new_df['Age1524_WhiteF'] = ini_df.loc[:, ['P012AVD30', 'P012AVD31', 'P012AVD32', 'P012AVD33', 'P012AVD34']].sum(axis=1)
        new_df['White_Females_All'] = ini_df.loc[:, 'P012AVD26']
    else:
        new_df['White_count'] = ini_df.loc[:, 'P12AD001']
        new_df['Age1524_WhiteM'] = ini_df.loc[:,['P12AD006', 'P12AD007', 'P12AD008', 'P12AD009', 'P12AD010']].sum(axis=1)
        new_df['White_Males_All'] = ini_df.loc[:, 'P12AD002']
        new_df['Age1524_WhiteF'] = ini_df.loc[:,['P12AD030', 'P12AD031', 'P12AD032', 'P12AD033', 'P12AD034']].sum(axis=1)
        new_df['White_Females_All'] = ini_df.loc[:, 'P12AD026']

    new_df['Pct_WYM'] = new_df['Age1524_WhiteM'] / new_df['White_Males_All']
    new_df['Pct_WYF'] = new_df['Age1524_WhiteF'] / new_df['White_Females_All']


def create_black_cols(ini_df, new_df, census_year):
    if census_year == '00':
        new_df['Black_count'] = ini_df.loc[:, 'P012BVD01']
        new_df['Age1524_BlackM'] = ini_df.loc[:, ['P012BVD06', 'P012BVD07', 'P012BVD08', 'P012BVD09', 'P012BVD10']].sum(axis=1)
        new_df['Black_Males_All'] = ini_df.loc[:, 'P012BVD02']
        new_df['Age1524_BlackF'] = ini_df.loc[:, ['P012BVD30', 'P012BVD31', 'P012BVD32', 'P012BVD33', 'P012BVD34']].sum(axis=1)
        new_df['Black_Females_All'] = ini_df.loc[:, 'P012BVD26']
    else:
        new_df['Black_count'] = ini_df.loc[:, 'P12BD001']
        new_df['Age1524_BlackM'] = ini_df.loc[:,['P12BD006', 'P12BD007', 'P12BD008', 'P12BD009', 'P12BD010']].sum(axis=1)
        new_df['Black_Males_All'] = ini_df.loc[:, 'P12BD002']
        new_df['Age1524_BlackF'] = ini_df.loc[:,['P12BD030', 'P12BD031', 'P12BD032', 'P12BD033', 'P12BD034']].sum(axis=1)
        new_df['Black_Females_All'] = ini_df.loc[:, 'P12BD026']


def create_hispanic_cols(ini_df, new_df, census_year):
    if census_year == '00':
        new_df['Hispanic_count'] = ini_df.loc[:, 'P012HVD01']
        new_df['Age1524_HispanicM'] = ini_df.loc[:, ['P012HVD06', 'P012HVD07', 'P012HVD08', 'P012HVD09', 'P012HVD10']].sum(axis=1)
        new_df['Hispanic_Males_All'] = ini_df.loc[:, 'P012HVD02']
        new_df['Age1524_HispanicF'] = ini_df.loc[:, ['P012HVD30', 'P012HVD31', 'P012HVD32', 'P012HVD33', 'P012HVD34']].sum(axis=1)
        new_df['Hispanic_Females_All'] = ini_df.loc[:, 'P012HVD26']
    else:
        new_df['Hispanic_count'] = ini_df.loc[:, 'P12HD001']
        new_df['Age1524_HispanicM'] = ini_df.loc[:,['P12HD006', 'P12HD007', 'P12HD008', 'P12HD009', 'P12HD010']].sum(axis=1)
        new_df['Hispanic_Males_All'] = ini_df.loc[:, 'P12HD002']
        new_df['Age1524_HispanicF'] = ini_df.loc[:,['P12HD030', 'P12HD031', 'P12HD032', 'P12HD033', 'P12HD034']].sum(axis=1)
        new_df['Hispanic_Females_All'] = ini_df.loc[:, 'P12HD026']


if __name__ == '__main__':
    data_files_path = '/Users/salma/Studies/Research/Criminal_Justice/research_projects/main_census_merge/data'
    ori_files_folder_name = 'new_fips_cols'
    mod_files_folder_name = 'new_census_variables'
    os.chdir(data_files_path)
    for census_dir in os.listdir():
        if not census_dir.startswith('.') and census_dir != 'wip_merge_files' and census_dir != 'crime_data': # to ignore hidden files such as .DS_Store and all census file

            # create a new df for everytime we move into new census dir so that the data from previous iteration is not carried over as was happening with 2000 county census file
            new_df = pd.DataFrame()

            census_folder_path = data_files_path + '/' + census_dir
            # move into the county/city census dir
            os.chdir(census_folder_path)

            # get a list of input files and capture their paths
            for sub_dir in os.listdir():
                if sub_dir == ori_files_folder_name:
                    sub_dir_path = census_folder_path + '/' + sub_dir
                    os.chdir(sub_dir_path)
                    for f in os.listdir():
                        # create input file path
                        in_file = sub_dir_path + '/' + f
                        # create output file path
                        census_type, census_year = fcg.get_census_type_year(in_file)
                        pop_type = in_file.split('/')[-1].split('_')[3]
                        initial_df = pd.read_csv(in_file)

                        # can create only POP100 column
                        if pop_type == 'P012' or pop_type == 'P12':
                            create_pop100_col(initial_df, new_df, census_year)
                        elif pop_type == 'P012A' or pop_type == 'P12A':
                            create_white_cols(initial_df, new_df, census_year)
                        elif pop_type == 'P012B' or pop_type == 'P12B':
                            create_black_cols(initial_df, new_df, census_year)
                        elif pop_type == 'P012H' or pop_type == 'P12H':
                            create_hispanic_cols(initial_df, new_df, census_year)

            gov_fips_yr_df = initial_df.loc[:, ['Govt_level', 'place_fips', 'placename', 'CNTY', 'STATEFP', 'YEAR']]
            final_df = gov_fips_yr_df.combine_first(new_df)

            # Rearrange the columns to match the respective positions in national_Census_1990_all file
            final_var_df = fcg.arrange_cols(final_df, final_df.columns.tolist(),
                                                                  {0:'Govt_level', 1:'place_fips', 2:'placename', 3:'CNTY', 4:'STATEFP', 5:'YEAR',
                                                                   6:'POP100', 7:'White_count', 8:'Black_count', 9:'Hispanic_count',
                                                                   10:'Age1524_WhiteM', 11:'White_Males_All', 12:'Age1524_WhiteF', 13:'White_Females_All',
                                                                   14:'Age1524_BlackM', 15:'Black_Males_All', 16:'Age1524_BlackF', 17:'Black_Females_All',
                                                                   18:'Hispanic_Males_All', 19:'Age1524_HispanicM', 20:'Age1524_HispanicF', 21:'Hispanic_Females_All',
                                                                   22:'Pct_WYM', 23:'Pct_WYF'})

            # overwrite the mod files folder if it already exists
            out_dir_path = census_folder_path + '/' + mod_files_folder_name
            if os.path.exists(out_dir_path):
                shutil.rmtree(out_dir_path)
            os.mkdir(out_dir_path)
            # os.makedirs(out_dir_path) - if subdirectories. Implement if needed like may be pass a list and mkdirs if list len > 1
            out_file = out_dir_path + '/' + 'new_vars_'+ census_dir + '.csv'
            #final_var_df.fillna(0)
            cf.write_updated_df_file(final_var_df, out_file)