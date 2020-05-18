import csv

geo_dict = {}

with open('data/census_county_2010/DEC_10_SF1_P12_with_ann.csv', 'r', encoding='utf-8', errors='ignore') as fr:
    '''
    To skip the 1st row which has VD01, VD02 etc.. as codes so that the next row which has more
    # clear column headers can be considered as the header row by dict reader
    '''
    # next(fr) - use it only for the original ann file which has 2 rows of headers

    fr_reader = csv.DictReader(fr)


    for line in fr_reader:

        '''
            Splitting the 'Geography' name value to get the type of geography
            First, splitting by ',' which would separate geography name and state and return these 2 in a list(1st list)
            Then, splitting the geography name (end element from end in the above list) by ' ' and returning them in a list(2nd list).
            Finally, the specific geography type would be the last element in the 2nd list
        '''

        geo_name = line['Geography'].split(',')[-2].split(' ')[-1]

        '''
            To get the count of each different type of geography
                If the geo_name is not already present in the dict, add it as a new 
                entry with value 1
                If it is present, then increment its value by 1
        '''
        if geo_name == 'Municipality':
            print(line['Geography'])

        if geo_name not in geo_dict:
            geo_dict[geo_name] = 1
        else:
            geo_dict[geo_name] += 1

print(geo_dict)

