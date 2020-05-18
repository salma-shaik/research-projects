import pandas as pd


def find_dtypes(file_path, census_type=None):
    if census_type is None: # Skipping the GEO.id,GEO.id2,GEO.display-label ..... rows for county files
        df = pd.DataFrame(pd.read_csv(file_path, skiprows=1))
    elif census_type == 'final_main' or '2010-county':
        df = pd.DataFrame(pd.read_csv(file_path))
    # print(df.dtypes)
    return df


# final main var file
# find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/Final_Main_Var_1990_2001.csv', 'final_main')
"""
ORI                   object
AGENCY                object
YEAR                   int64
ORICOUNT               int64
FIPS_STATE             int64
FIPS_COUNTY            int64
POP                  float64
GROUP                 object
CGOVTYPE               int64
PER_CAPITA_INCOME    float64
EMPLOYMENT           float64
STCO_FIPS              int64
PROP_MALE            float64
PROP_AGE1524         float64
PROP_NONWHITE        float64
COUNTYPOP              int64
EMPLOYMENT_RATE      float64
VIOLENT_SUM            int64
VIOLENT_RATE         float64
PROPERTY_RATE        float64
MURDER_RATE          float64
MANSLAUGHTER_RATE    float64
RAPE_RATE            float64
ROBBERY_RATE         float64
BURGLARY_RATE        float64
LARCENY_RATE         float64
VEHICLE_RATE         float64
AGG_ASSAULT_RATE     float64
FIPS_PLACE             int64
ALLCOUNTY              int64
SIZECAT                int64
OFFICERS             float64
OFFICER_RATE         float64
TOT_ALL              float64
TOT_FELONIES         float64
TOT_NONUCR           float64
PROP_MISD            float64
MISD_PER_OFC         float64
MISD_Arrests         float64
MISD_Rate            float64
DRUG_Rate            float64
SQRTPOP              float64
NONWHITE             float64
AGE_1524             float64
dtype: object
"""

# 2000 county file
# find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2000/DEC_00_SF1_P012_with_ann.csv', 2000)
#print(df.dtypes)
"""
DEC_00_SF1_P012_with_ann.csv
GEO.id               object
GEO.id2              object

Id                             object
Id2                             int64
Geography                      object
Total:                          int64
Male:                           int64
Male: - Under 5 years           int64
Male: - 5 to 9 years            int64
Male: - 10 to 14 years          int64
Male: - 15 to 17 years          int64
Male: - 18 and 19 years         int64
Male: - 20 years                int64
Male: - 21 years                int64
Male: - 22 to 24 years          int64
Male: - 25 to 29 years          int64
Male: - 30 to 34 years          int64
Male: - 35 to 39 years          int64
Male: - 40 to 44 years          int64
Male: - 45 to 49 years          int64
Male: - 50 to 54 years          int64
Male: - 55 to 59 years          int64
Male: - 60 and 61 years         int64
Male: - 62 to 64 years          int64
Male: - 65 and 66 years         int64
Male: - 67 to 69 years          int64
Male: - 70 to 74 years          int64
Male: - 75 to 79 years          int64
Male: - 80 to 84 years          int64
Male: - 85 years and over       int64
Female:                         int64
Female: - Under 5 years         int64
Female: - 5 to 9 years          int64
Female: - 10 to 14 years        int64
Female: - 15 to 17 years        int64
Female: - 18 and 19 years       int64
Female: - 20 years              int64
Female: - 21 years              int64
Female: - 22 to 24 years        int64
Female: - 25 to 29 years        int64
Female: - 30 to 34 years        int64
Female: - 35 to 39 years        int64
Female: - 40 to 44 years        int64
Female: - 45 to 49 years        int64
Female: - 50 to 54 years        int64
Female: - 55 to 59 years        int64
Female: - 60 and 61 years       int64
Female: - 62 to 64 years        int64
Female: - 65 and 66 years       int64
Female: - 67 to 69 years        int64
Female: - 70 to 74 years        int64
Female: - 75 to 79 years        int64
Female: - 80 to 84 years        int64
Female: - 85 years and over     int64
dtype: object
"""

# 2010 county file
# find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_county_2010/DEC_10_SF1_P12_with_ann.csv', '2010-county')
"""
Id                             object
Id2                             int64
Geography                      object
Total:                         object
Male:                           int64
Male: - Under 5 years           int64
Male: - 5 to 9 years            int64
Male: - 10 to 14 years          int64
Male: - 15 to 17 years          int64
Male: - 18 and 19 years         int64
Male: - 20 years                int64
Male: - 21 years                int64
Male: - 22 to 24 years          int64
Male: - 25 to 29 years          int64
Male: - 30 to 34 years          int64
Male: - 35 to 39 years          int64
Male: - 40 to 44 years          int64
Male: - 45 to 49 years          int64
Male: - 50 to 54 years          int64
Male: - 55 to 59 years          int64
Male: - 60 and 61 years         int64
Male: - 62 to 64 years          int64
Male: - 65 and 66 years         int64
Male: - 67 to 69 years          int64
Male: - 70 to 74 years          int64
Male: - 75 to 79 years          int64
Male: - 80 to 84 years          int64
Male: - 85 years and over       int64
Female:                         int64
Female: - Under 5 years         int64
Female: - 5 to 9 years          int64
Female: - 10 to 14 years        int64
Female: - 15 to 17 years        int64
Female: - 18 and 19 years       int64
Female: - 20 years              int64
Female: - 21 years              int64
Female: - 22 to 24 years        int64
Female: - 25 to 29 years        int64
Female: - 30 to 34 years        int64
Female: - 35 to 39 years        int64
Female: - 40 to 44 years        int64
Female: - 45 to 49 years        int64
Female: - 50 to 54 years        int64
Female: - 55 to 59 years        int64
Female: - 60 and 61 years       int64
Female: - 62 to 64 years        int64
Female: - 65 and 66 years       int64
Female: - 67 to 69 years        int64
Female: - 70 to 74 years        int64
Female: - 75 to 79 years        int64
Female: - 80 to 84 years        int64
Female: - 85 years and over     int64
dtype: object

"""

# 2000 city file
# find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2000/DEC_00_SF1_P012_with_ann.csv')
"""
Id                             object
Id2                             int64
Geography                      object
Total:                          int64
Male:                           int64
Male: - Under 5 years           int64
Male: - 5 to 9 years            int64
Male: - 10 to 14 years          int64
Male: - 15 to 17 years          int64
Male: - 18 and 19 years         int64
Male: - 20 years                int64
Male: - 21 years                int64
Male: - 22 to 24 years          int64
Male: - 25 to 29 years          int64
Male: - 30 to 34 years          int64
Male: - 35 to 39 years          int64
Male: - 40 to 44 years          int64
Male: - 45 to 49 years          int64
Male: - 50 to 54 years          int64
Male: - 55 to 59 years          int64
Male: - 60 and 61 years         int64
Male: - 62 to 64 years          int64
Male: - 65 and 66 years         int64
Male: - 67 to 69 years          int64
Male: - 70 to 74 years          int64
Male: - 75 to 79 years          int64
Male: - 80 to 84 years          int64
Male: - 85 years and over       int64
Female:                         int64
Female: - Under 5 years         int64
Female: - 5 to 9 years          int64
Female: - 10 to 14 years        int64
Female: - 15 to 17 years        int64
Female: - 18 and 19 years       int64
Female: - 20 years              int64
Female: - 21 years              int64
Female: - 22 to 24 years        int64
Female: - 25 to 29 years        int64
Female: - 30 to 34 years        int64
Female: - 35 to 39 years        int64
Female: - 40 to 44 years        int64
Female: - 45 to 49 years        int64
Female: - 50 to 54 years        int64
Female: - 55 to 59 years        int64
Female: - 60 and 61 years       int64
Female: - 62 to 64 years        int64
Female: - 65 and 66 years       int64
Female: - 67 to 69 years        int64
Female: - 70 to 74 years        int64
Female: - 75 to 79 years        int64
Female: - 80 to 84 years        int64
Female: - 85 years and over     int64
dtype: object
"""

# 2010 city file
# find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann.csv')
"""
Id                             object
Id2                             int64
Geography                      object
Total:                         object
Male:                           int64
Male: - Under 5 years           int64
Male: - 5 to 9 years            int64
Male: - 10 to 14 years          int64
Male: - 15 to 17 years          int64
Male: - 18 and 19 years         int64
Male: - 20 years                int64
Male: - 21 years                int64
Male: - 22 to 24 years          int64
Male: - 25 to 29 years          int64
Male: - 30 to 34 years          int64
Male: - 35 to 39 years          int64
Male: - 40 to 44 years          int64
Male: - 45 to 49 years          int64
Male: - 50 to 54 years          int64
Male: - 55 to 59 years          int64
Male: - 60 and 61 years         int64
Male: - 62 to 64 years          int64
Male: - 65 and 66 years         int64
Male: - 67 to 69 years          int64
Male: - 70 to 74 years          int64
Male: - 75 to 79 years          int64
Male: - 80 to 84 years          int64
Male: - 85 years and over       int64
Female:                         int64
Female: - Under 5 years         int64
Female: - 5 to 9 years          int64
Female: - 10 to 14 years        int64
Female: - 15 to 17 years        int64
Female: - 18 and 19 years       int64
Female: - 20 years              int64
Female: - 21 years              int64
Female: - 22 to 24 years        int64
Female: - 25 to 29 years        int64
Female: - 30 to 34 years        int64
Female: - 35 to 39 years        int64
Female: - 40 to 44 years        int64
Female: - 45 to 49 years        int64
Female: - 50 to 54 years        int64
Female: - 55 to 59 years        int64
Female: - 60 and 61 years       int64
Female: - 62 to 64 years        int64
Female: - 65 and 66 years       int64
Female: - 67 to 69 years        int64
Female: - 70 to 74 years        int64
Female: - 75 to 79 years        int64
Female: - 80 to 84 years        int64
Female: - 85 years and over     int64
dtype: object
"""

# df = find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann.csv')
# print(df['Id2'].dtype)

"""
df = find_dtypes('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/data/census_cities_2010/DEC_10_SF1_P12_with_ann.csv')
# to get the type of each cell in the Total column
df['Total_type'] = df['Total:'].apply(lambda x: type(x).__name__)
df.to_csv('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/tests/test_data_files/2010_cities_census_total_col_dtypes.csv', encoding='utf-8')

# Find unique dtypes from 2010_cities_census_total_col_dtypes file since we were getting "sys:1: DtypeWarning: Columns (3) have mixed types. Specify dtype option on import or set low_memory=False."
# warning when trying to find the dtypes.
city_df = pd.read_csv('C:/Users/sshaik2/PycharmProjects/projects/research-projects/main_census_merge/tests/test_data_files/2010_cities_census_total_col_dtypes.csv')
print(set(city_df['Total_type'])) # {'str', 'int'}

print(df['Total_type']) # some string values fpr ex: Id2=103076, 26 row index Total: is 53380(r38811)
"""



# National_Census_1990_All dtypes
df = pd.DataFrame(pd.read_excel('C:/Users/sshaik2/Criminal_Justice/Projects/main_census_merge/data/National_Census_1990_All.xlsx'))
print(df.head())
"""
Govt_level              int64
place_fips              int64
placename              object
CNTY                  float64
STATEFP                 int64
POP100                  int64
White_count             int64
Black_count             int64
Other_count             int64
Hispan_allcount         int64
Age1524_WhiteM          int64
White_Males_All         int64
Age1524_WhiteF          int64
White_Females_All       int64
Age1524_BlackM          int64
Black_Males_All         int64
Age1524_BlackF          int64
Black_Females_All       int64
Hispan_Males_All        int64
Age1524_HispanM         int64
Age1524_HispanF         int64
Hispan_Females_All      int64
Other_Males_All         int64
Age1524_OtherM          int64
Age1524_OtherF          int64
Other_Females_All       int64
Pct_WYM               float64
Pct_WYF               float64
dtype: object
"""