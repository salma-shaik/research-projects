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


def consolidate_90_files():
    cnty_90 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/1990/renamed_cols_eco_cen_90_cnty_initial.csv')
    cnty_90.drop_duplicates(subset=['STATEFP', 'CNTY'], inplace=True)
    cnty_subd_90 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/1990/renamed_cols_eco_cen_90_cnty_subd_initial.csv')
    cnty_subd_90.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)
    place_90 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/1990/renamed_cols_eco_cen_90_place_initial.csv')
    place_90.drop_duplicates(subset=['STATEFP', 'place_fips'],  inplace=True)

    eco_90 = cnty_90.append([place_90, cnty_subd_90], sort=False)
    # shape check passed
    eco_90.to_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/1990/eco_90.csv',
        index=False)


def consolidate_00_files():
    cnty_00 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2000/renamed_cols_eco_cen_00_cnty_initial.csv')
    cnty_00.drop_duplicates(subset=['STATEFP', 'CNTY'], inplace=True)
    cnty_subd_00 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2000/renamed_cols_eco_cen_00_cnty_subd_initial.csv')
    cnty_subd_00.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)
    place_00 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2000/renamed_cols_eco_cen_00_place_initial.csv')
    place_00.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    eco_00 = cnty_00.append([place_00, cnty_subd_00], sort=False)
    # shape check passed
    eco_00.to_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2000/eco_00.csv',
        index=False)

    # if eco_00.shape[0] == cnty_00.shape[0] + cnty_subd_00.shape[0] + place_00.shape[0]:
    #     print('shape mathced')


def consolidate_10_files():

    ### append till and from variable files - shape matched
    # cnty
    cnty1 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/county/renamed_cols_eco_cen_10_cnty_tillst50_cnty21_till_B23001_093E_initial.csv')
    cnty2 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/county/renamed_cols_eco_cen_10_cnty_4mst50cnty23_till_B23001_093E_initial.csv')
    cnty_1_2 = cnty1.append(cnty2, sort=False, ignore_index=True)
    cnty_1_2.drop_duplicates(subset=['STATEFP', 'CNTY'])
    cnty3 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/county/renamed_cols_eco_cen_10_cnty_4mB23001_100E_initial.csv')
    cnty3.drop_duplicates(subset=['STATEFP', 'CNTY'])
    cnty = pd.merge(cnty_1_2, cnty3, on=['STATEFP', 'CNTY'])
    cnty = cnty.rename({'placename_x': 'placename'}, axis='columns')
    cnty.drop(['placename_y'], axis=1, inplace=True)

    cnty.to_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/county/eco_10_cnty.csv',
                index=False)

    # cnty_subd
    cnty_subd1 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/cnty_subd/renamed_cols_eco_cen_10_cnty_subd_initial_till_B23001_093E.csv')
    cnty_subd2 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/cnty_subd/renamed_cols_eco_cen_10_cnty_subd_4mst37cn171_till_B23001_093E_initial.csv')
    cnty_subd_1_2 = cnty_subd1.append(cnty_subd2, sort=False, ignore_index=True)
    cnty_subd_1_2.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    cnty_subd3 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/cnty_subd/renamed_cols_eco_cen_10_cnty_subd_4mB23001_100E_initial.csv')

    cnty_subd3.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)
    cnty_subd = pd.merge(cnty_subd_1_2, cnty_subd3, on=['STATEFP', 'place_fips'])

    cnty_subd = cnty_subd.rename({'placename_x':'placename', 'CNTY_x':'CNTY'}, axis='columns')
    cnty_subd.drop(['placename_y', 'CNTY_y', 'C24010_002E', 'B23001_001E'], axis=1, inplace=True)
    cnty_subd.to_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/cnty_subd/eco_10_cnty_subd.csv',
        index=False)

    # place
    plc1 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/place/renamed_cols_eco_cen_10_place_till_B23001_093E_initial.csv')
    plc1.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    plc2 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/place/renamed_cols_eco_cen_10_place_4mB23001_100E_initial.csv')
    plc2.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    plc = pd.merge(plc1,plc2, on=['STATEFP', 'place_fips'])
    plc = plc.rename({'placename_x': 'placename'}, axis='columns')
    plc.drop(['placename_y', 'C24010_002E', 'B23001_001E'], axis=1,inplace=True)

    plc.to_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/place/eco_10_place.csv',
        index=False)

    ### Now consolidate eco cnty, cnty subd, place files
    cnty_10 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/county/eco_10_cnty.csv')
    cnty_subd_10 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/cnty_subd/eco_10_cnty_subd.csv')
    plc_10 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/place/eco_10_place.csv')
    eco_10 = cnty_10.append([cnty_subd_10, plc_10], sort=False, ignore_index=True)
    eco_10.to_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/eco_10.csv',
        index=False)

    if eco_10.shape[0] == cnty.shape[0] + cnty_subd.shape[0] + plc.shape[0]:
        print('shape mathced')



def consolidate_15_files():
    ### append till and from variable files - shape matched

    #####  cnty  ######
    # append all county till_B23001_093E files
    till_fl1 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed_cols_eco_cen_15_cnty_till_st2_cnty261_till_B23001_093E_initial.csv')
    till_fl2 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed/renamed_cols_eco_cen_15_cnty_afterst2_cnty270_till_B23001_093E_initial.csv')
    till_fl3 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed/renamed_cols_eco_cen_15_cnty_4mst24_cnty35_till_B23001_093E_initial.csv')
    till_fl4 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed/renamed_cols_eco_cen_15_cnty_4mst26_cnty139_till_B23001_093E_initial.csv')
    till_fl5 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed/renamed_cols_eco_cen_15_cnty_4mst35_cnty28_till_B23001_093E_initial.csv')
    till_fl6 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed/renamed_cols_eco_cen_15_cnty_4mst46_cnty113_till_B23001_093E_initial.csv')
    till_fl7 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/till_B23001_093E/renamed/renamed_cols_eco_cen_15_cnty_4mst51_cnty520_till_B23001_093E_initial.csv')

    till_fl = till_fl1.append([till_fl2,till_fl3,till_fl4,till_fl5,till_fl6,till_fl7], sort=False, ignore_index=True)
    till_fl.drop_duplicates(subset=['STATEFP', 'CNTY'], inplace=True)

    # append all county 4m_B23001_100E files
    from_fl1 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/4m_B23001_100E/renamed_cols_eco_cen_15_cnty_4mB23001_100E_initial_1.csv')
    from_fl2 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/4m_B23001_100E/renamed/renamed_cols_eco_cen_15_cnty_4mB23001_100E_initial_2.csv')
    from_fl3 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/4m_B23001_100E/renamed/renamed_cols_eco_cen_15_cnty_4mB23001_100E_initial_3.csv')
    from_fl4 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/4m_B23001_100E/renamed/renamed_cols_eco_cen_15_cnty_4mB23001_100E_initial_4.csv')
    from_fl5 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/4m_B23001_100E/renamed/renamed_cols_eco_cen_15_cnty_4mB23001_100E_initial_5.csv')

    from_fl = from_fl1.append([from_fl2,from_fl3,from_fl4,from_fl5], sort=False, ignore_index=True)
    from_fl.drop_duplicates(subset=['STATEFP', 'CNTY'], inplace=True)

    ## now merge till and from to create final eco_15_cnty file
    cnty = pd.merge(till_fl, from_fl, on=['STATEFP', 'CNTY'])
    cnty = cnty.rename({'placename_x': 'placename'}, axis='columns')
    cnty.drop(['placename_y', 'C24010_002E', 'B23001_001E'], axis=1, inplace=True)
    cnty.to_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/eco_15_cnty.csv', index=False)


    ######### cnty_subd ###########
    cd_till1 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_1.csv')
    cd_till2 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_2.csv')
    cd_till3 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_3.csv')
    cd_till4 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_4.csv')
    cd_till5 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_5.csv')
    cd_till6 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_6.csv')
    cd_till7 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/till_B23001_093E/renamed_cols_eco_cen_15_cnty_subd_till_B23001_093E_initial_7.csv')

    cd_till = cd_till1.append([cd_till2,cd_till3,cd_till4,cd_till5,cd_till6,cd_till7], sort=False, ignore_index=True)
    cd_till.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    cd_from1 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/4m_B23001_100E/renamed_cols_eco_cen_15_cnty_subd_4mB23001_100E_initial_1.csv')
    cd_from2 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/4m_B23001_100E/renamed_cols_eco_cen_15_cnty_subd_4mB23001_100E_initial_2.csv')
    cd_from3 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/4m_B23001_100E/renamed_cols_eco_cen_15_cnty_subd_4mB23001_100E_initial_3.csv')
    cd_from4 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/4m_B23001_100E/renamed_cols_eco_cen_15_cnty_subd_4mB23001_100E_initial_4.csv')
    cd_from5 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/4m_B23001_100E/renamed_cols_eco_cen_15_cnty_subd_4mB23001_100E_initial_5.csv')

    cd_from = cd_from1.append([cd_from2,cd_from3,cd_from4,cd_from5],sort=False, ignore_index=True)
    cd_from.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    ## concat cd_till and cd_from to get final eco_15_cnty_subd
    cd = pd.merge(cd_till, cd_from, on=['STATEFP', 'place_fips'])

    cd = cd.rename({'placename_x': 'placename', 'CNTY_x': 'CNTY'}, axis='columns')
    cd.drop(['placename_y', 'CNTY_y', 'C24010_002E', 'B23001_001E'], axis=1, inplace=True)

    cd.to_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/eco_15_cnty_subd.csv',
              index=False)


    ###### place ########
    plc1 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/place/renamed_cols_eco_cen_15_place_till_B23001_093E_initial_1.csv')
    plc1.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    plc2 = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/place/renamed_cols_eco_cen_15_place_from B23001_100E_initial_1.csv')
    plc2.drop_duplicates(subset=['STATEFP', 'place_fips'], inplace=True)

    plc=pd.merge(plc1, plc2, on=['STATEFP', 'place_fips'])
    plc = plc.rename({'placename_x': 'placename'}, axis='columns')
    plc.drop(['placename_y', 'C24010_002E', 'B23001_001E'], axis=1, inplace=True)

    plc.to_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/place/eco_15_place.csv',
               index=False)

    ### Now consolidate eco cnty, cnty subd, place files
    cnty_15 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/county/eco_15_cnty.csv')
    cnty_subd_15 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/cnty_subd/eco_15_cnty_subd.csv')
    plc_15 = pd.read_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/place/eco_15_place.csv')
    eco_15 = cnty_15.append([cnty_subd_15, plc_15], sort=False, ignore_index=True)
    eco_15.to_csv(
        '/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/eco_15.csv',
        index=False)

    if eco_15.shape[0] == cnty_15.shape[0] + cnty_subd_15.shape[0] + plc_15.shape[0]:
        print('shape mathced')


def create_new_10_15_vars(df, year):
    df['emp_forces_male'] = df.loc[:,['emp_forces_male_16-19','emp_forces_male_20-21','emp_forces_male_22-24','emp_forces_male_25-29','emp_forces_male_30-34',
                            'emp_forces_male_35-44', 'emp_forces_male_45-54','emp_forces_male_55-59','emp_forces_male_60-61','emp_forces_male_62-64']].sum(axis=1)

    df['emp_civ_male'] = df.loc[:, ['emp_civ_male_16-19','emp_civ_male_20-21','emp_civ_male_22-24','emp_civ_male_25-29','emp_civ_male_30-34','emp_civ_male_35-44',
                                    'emp_civ_male_45-54','emp_civ_male_55-59','emp_civ_male_60-61','emp_civ_male_62-64']].sum(axis=1)

    df['emp_forces_female'] = df.loc[:, ['emp_forces_female_16-19', 'emp_forces_female_20-21', 'emp_forces_female_22-24', 'emp_forces_female_25-29', 'emp_forces_female_30-34',
                                       'emp_forces_female_35-44', 'emp_forces_female_45-54', 'emp_forces_female_55-59', 'emp_forces_female_60-61', 'emp_forces_female_62-64']].sum(axis=1)

    df['emp_civ_female'] = df.loc[:,['emp_civ_female_16-19','emp_civ_female_20-21','emp_civ_female_22-24','emp_civ_female_25-29','emp_civ_female_30-34','emp_civ_female_35-44',
                                     'emp_civ_female_45-54','emp_civ_female_55-59','emp_civ_female_60-61','emp_civ_female_62-64']].sum(axis=1)

    ## delete the individual cols
    df.drop(['emp_forces_male_16-19','emp_forces_male_20-21','emp_forces_male_22-24','emp_forces_male_25-29','emp_forces_male_30-34','emp_forces_male_35-44',
             'emp_forces_male_45-54','emp_forces_male_55-59','emp_forces_male_60-61','emp_forces_male_62-64', 'emp_civ_male_16-19','emp_civ_male_20-21',
             'emp_civ_male_22-24','emp_civ_male_25-29','emp_civ_male_30-34','emp_civ_male_35-44','emp_civ_male_45-54','emp_civ_male_55-59','emp_civ_male_60-61',
             'emp_civ_male_62-64','emp_forces_female_16-19', 'emp_forces_female_20-21', 'emp_forces_female_22-24', 'emp_forces_female_25-29', 'emp_forces_female_30-34',
             'emp_forces_female_35-44', 'emp_forces_female_45-54', 'emp_forces_female_55-59', 'emp_forces_female_60-61', 'emp_forces_female_62-64','emp_civ_female_16-19',
             'emp_civ_female_20-21', 'emp_civ_female_22-24', 'emp_civ_female_25-29', 'emp_civ_female_30-34', 'emp_civ_female_35-44','emp_civ_female_45-54',
             'emp_civ_female_55-59', 'emp_civ_female_60-61', 'emp_civ_female_62-64', 'emp_civ_male_65-69', 'emp_civ_male_70-74','emp_civ_male_75_and_over',
             'emp_civilian_male_white_alone_above_64', 'emp_civilian_male_white_above_64', 'emp_civilian_female_white_above_64', 'emp_civilian_male_black_above_64',
             'emp_civilian_female_black_above_64', 'emp_civilian_male_hisp_above_64', 'emp_civilian_female_hisp_above_64', 'emp_civ_female_65-69',
             'emp_civ_female_70-74', 'emp_civ_female_75_and_over', 'emp_civilian_female_white_alone_above_64'], axis=1, inplace=True)

    df.to_csv(f'/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/economic_data_{year}.csv', index=False)

### Update col names
#var_mapping_df = pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/eco_files_var_mapping.csv')
#read_eco_data_files('/Users/salma/Research/research-projects/us-crime-analytics/new_eco_cen_vars', var_mapping_df)


### Consolidate 1990 files
# consolidate_90_files()

### Consolidate 2000 files
# consolidate_00_files()

### Consolidate 2010 files
# consolidate_10_files()

### Consolidate 2015 files
# consolidate_15_files()

create_new_10_15_vars(pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2010/eco_10.csv'), year=2010)
create_new_10_15_vars(pd.read_csv('/Users/salma/Research/research-projects/us-crime-analytics/data/economic/new_eco_cen_vars/2015/eco_15.csv'), year=2015)