import pandas as pd
import os


def rename_cols(ip_fl_path, mapping_dict, fl_name):
    # Had to initilaize here before using in try block coz was throwing variable used before initializing error
    eco_data_df = pd.DataFrame()
    try:
        # using ISO-8859-1 to address some encode/decode issues
        eco_data_df = pd.read_csv(ip_fl_path, encoding = "ISO-8859-1")
    except Exception as ex:
        print(ex)
        print('Error reading file: ', ip_fl_path)

    # rename df column names using mapping dict
    eco_data_df_renamed = eco_data_df.rename(columns=mapping_dict)

    # write the output file
    eco_data_df_renamed.to_csv('/Users/salma/Research/research-projects/us-crime-analytics/updated_eco_files/renamed_cols' + '/' + 'renamed_cols_' + fl_name, index=False)


def read_eco_data_files(dir_path, mapping_df):
    os.chdir(dir_path)

    yr_dirs = os.listdir()
    for yr_dir in yr_dirs:
        dir_name = yr_dir

        # ignore .DS_Store files
        if yr_dir != '.DS_Store':
            # convert the mapping dfs to dict
            mapping_dict = dict(zip(mapping_df[f'{yr_dir}_Existing_Var_Name'], mapping_df[f'{yr_dir}_New_Var_Name']))
            #del mapping_dict[np.nan]

           # get the current year path
            year_path = dir_path + '/' + yr_dir

            #change to the current year directory
            os.chdir(year_path)

            yr_entries = os.listdir()
            #iterate through every entry in the year dir
            for entry in yr_entries:
                '''
                # looping through the below
                county
                cnty_subd
                place
                eco_cen_00_place_initial.csv
                eco_cen_00_cnty_initial.csv
                eco_cen_00_cnty_subd_initial.csv
                county
                cnty_subd
                place
                eco_cen_90_cnty_initial.csv
                eco_cen_90_place_initial.csv
                eco_cen_90_cnty_subd_initial.csv
                '''

                if entry != '.DS_Store':
                    # 2010 and 2015 have subdirs again. So need to navigate into them if they are
                    yr_entry_path = year_path + '/' + entry
                    if os.path.isdir(yr_entry_path):
                        os.chdir(yr_entry_path)
                        for data_fle in os.listdir():
                            if data_fle != '.DS_Store':
                                # 2015 directory again has till and from subdirectories. So need to navigate into them when present
                                data_fle_path = yr_entry_path + '/' + data_fle
                                if os.path.isdir(data_fle_path):
                                    os.chdir(data_fle_path)
                                    # now I know that there are no more subdirectories under this. so just calling rename function directly.
                                    for subfile in os.listdir():
                                        if subfile != '.DS_Store':
                                            rename_cols(ip_fl_path=data_fle_path+'/'+subfile, mapping_dict=mapping_dict, fl_name = subfile)
                                else:
                                    rename_cols(ip_fl_path=data_fle_path, mapping_dict=mapping_dict, fl_name=data_fle)
                    else:
                        rename_cols(ip_fl_path=yr_entry_path, mapping_dict=mapping_dict, fl_name=entry)

var_mapping_df = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/eco_files_var_mapping.csv')
read_eco_data_files('/Users/salma/Research/research-projects/us-crime-analytics/new_eco_cen_vars', var_mapping_df)