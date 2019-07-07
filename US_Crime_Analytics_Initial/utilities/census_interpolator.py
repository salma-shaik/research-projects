import pandas as pd
from datetime import datetime


def interpolate_census():
    print("########## Start: ", datetime.now().time())
    dec_cen_all = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/merge_files/Census_90-15_Final_Sorted.csv')

    # Create an empty df to append the original rows and empty rows for every iteration of the original nat_cen_all df.
    dec_cen_all_int = pd.DataFrame(columns=dec_cen_all.columns)

    for row in dec_cen_all.itertuples():
        # ????? ###
        dec_cen_all_int = dec_cen_all_int.append(pd.Series(row[1:], index=dec_cen_all.columns), ignore_index=True)
        # append 4 rows after 2015 for 14, 13, 12, 11
        if row.YEAR == 2015:
            for i in range(4):
                dec_cen_all_int = dec_cen_all_int.append(pd.Series(), ignore_index=True)
        # append 9 empty rows if the year is != 1990 and 2015 coz we are interpolating till 1990.
        if row.YEAR != 1990 and row.YEAR != 2015:
            for i in range(9):
                dec_cen_all_int = dec_cen_all_int.append(pd.Series(), ignore_index=True)

    dec_cen_all_int.drop(['YEAR'], axis=1, inplace=True)
    # Create all years between 90-15
    years = pd.DataFrame(
        {'census_year': [2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001,
                        2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990]})

    # ffill constant values so that they are copied for in between decennial years
    dec_cen_all_int.fillna(method='ffill', inplace=True)

    census_year = pd.concat([years] * 14831,
                           ignore_index=True)  # 14831 records(ORIs) in each normalized census files. So all these years for each of the ORI. Total 385606

    dec_cen_all_int = pd.concat([dec_cen_all_int, census_year], axis=1)

    # Interpolate. This fills all the NaN rows between 2 given years that were added above.
    dec_cen_all_int = dec_cen_all_int.interpolate(method='linear', axis=0)

    dec_cen_all_int = dec_cen_all_int.sort_values(by=['ORI', 'census_year'], ascending=[True, False])
    dec_cen_all_int.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/interpolated_files/Census_Interpolated_All_Vars_Together.csv', index=False)

    print("########## End: ", datetime.now().time())

interpolate_census()