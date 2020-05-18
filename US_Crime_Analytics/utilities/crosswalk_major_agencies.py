import pandas as pd

crswlk_df = pd.read_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/crosswalk_improved_2006.csv')
print('crosswalk_improved_2006 ', crswlk_df.shape[0])

########## TO-DO:  Use UPOPCOV ##########
# Drop the records where UPOPCOV == 99999999
crswlk_df = crswlk_df[crswlk_df.UPOPCOV != 9999999]
crswlk_df = crswlk_df[crswlk_df.UPOPCOV != 0]
crswlk_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_without_99999999.csv')
print('crosswalk_without_99999999 ', crswlk_df.shape[0])

# Drop the records with blank ORIs or UPOPCOV
crswlk_df.dropna(subset=['ORI', 'UPOPCOV'], inplace=True)
crswlk_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_without_99999999_blankORIs_dropped.csv', index=False)
print('crosswalk_without_99999999_blankORIs_dropped ', crswlk_df.shape[0])


#### TO-DO: Remove the ones with 0 UPOCOV
# Get only those crswlk file records whose cgovtype is 1,2,3
crswlk_123 = crswlk_df.loc[crswlk_df['CGOVTYPE'].isin([1, 2, 3])]
crswlk_123.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_without_99999999_blankORIs_dropped_123.csv', index=False)
print('crosswalk_without_99999999_blankORIs_dropped_123 ', crswlk_123.shape[0])

"""
    Sort by state and place fips and then by population(descending) - to identify major agencies. 
    Keep the record with highest population - THESE SHOULD BE UNIQUE
"""
crswlk_123.sort_values(by=['fips_state', 'fips_place', 'UPOPCOV'], ascending=[True, True, False], inplace=True)
crswlk_123.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_without_99999999_blankORIs_dropped_123_sorted.csv', index=False)
print('crosswalk_without_99999999_blankORIs_dropped_123_sorted ', crswlk_123.shape[0])

# Drop duplicates so that only the highest population record is retained for a given agency.
crswlk_major = crswlk_123.drop_duplicates(subset=['fips_state', 'fips_place'])
crswlk_major.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/cleaned_files/crosswalk/crosswalk_major_agencies.csv',index=False)
print('crosswalk_major_agencies ', crswlk_major.shape[0])

# Write the final df to a csv
#crswlk_df.to_csv('/Users/salma/Studies/Research/Criminal_Justice/research_projects/US_Crime_Analytics/data/wip_merge_files/crosswalk_major_agencies.csv', index=False)
