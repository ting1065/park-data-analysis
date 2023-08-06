'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
data_analysis_functions.py
Fengting Tang
'''


import pandas as pd
from src.neighbourhood_population_class import NeighbourhoodPopulation
from src.park_class import Park

UNIT_FOR_AVERAGING = 1000
ROUNDED_DECIMAL = 2
AGE_GROUP_0_14 = "0 - 14"
AGE_GROUP_15_64 = "15 - 64"
AGE_GROUP_65_ABOVE = "65 -"
AGE_GROUP_ALL = "All"

def make_neighbourhood_population_object_list(census_data_cleaned):
    '''
    Function -- make_neighbourhood_population_object_list:
        creat NeighbourhoodPopulation objects according to 
        the given data, and add the objects to a list
    Parameters:
        census_data_cleaned -- a list of lists of strings and integers
    return:
        return a list of NeighbourhoodPopulation objects
    Raises:
        TypeError -- when census_data_cleaned is not a list
    '''
    if not isinstance(census_data_cleaned, list):
            raise TypeError("census_data_cleaned for"\
                            "make_neighbourhood_population_object_list() must be a list")

    neighbourhood_population_object_list = []

    for i in range(len(census_data_cleaned[0])):

        neighbourhood = census_data_cleaned[0][i]
        population_0_14 = census_data_cleaned[1][i]
        population_15_64 = census_data_cleaned[2][i]
        population_65_above = census_data_cleaned[3][i]
        population_total = population_0_14 + population_15_64 +population_65_above

        neighbourhood_population = NeighbourhoodPopulation(neighbourhood, population_0_14,
                                    population_15_64, population_65_above, population_total)
        neighbourhood_population_object_list.append(neighbourhood_population)

    return neighbourhood_population_object_list

def make_park_object_list(park_data_cleaned):
    '''
    Function -- make_park_object_list:
        creat Park objects according to the given data, and add
        the objects to a list
    Parameters:
        park_data_cleaned -- a list of lists of strings and floats
    return:
        return a list of Park objects
    Raises:
        TypeError -- when park_data_cleaned is not a list
    '''
    if not isinstance(park_data_cleaned, list):
            raise TypeError("park_data_cleaned for make_park_object_list()"\
                            " must be a list")
    park_object_list = []

    for i in park_data_cleaned:

        park_name = i[0]
        neighbourhood = i[1]
        area_in_hectare = i[2]
        
        park = Park(park_name, neighbourhood, area_in_hectare)
        park_object_list.append(park)

    return park_object_list

def make_neighbourhood_list(neighbourhood_population_object_list):
    '''
    Function -- make_neighbourhood_list
        make a list of neighbourhood names from the NeighbourhoodPopulation
        objects in the given lists
    Parameters:
        neighbourhood_population_object_list -- a list of NeighbourhoodPopulation objects
    Return:
        return a list of strings that are neighbourhood names
    Raises:
        TypeError -- when the argument is not a list
        ValueError -- when given list's elements are not all NeighbourhoodPopulation objects
    '''
    if not isinstance(neighbourhood_population_object_list, list):
        raise TypeError("the argument for make_neighbourhood_list()"\
                        " must be a list.")

    for i in neighbourhood_population_object_list:
        if not isinstance(i, NeighbourhoodPopulation):
            raise ValueError("the argument for make_neighbourhood_list() "\
                             "must be a list of NeighbourhoodPopulation objects.")

    neighbourhood_list = []

    for i in neighbourhood_population_object_list:
        neighbourhood_list.append(i.neighbourhood)

    return neighbourhood_list

def make_population_list(neighbourhood_population_object_list, age_group):
    '''
    Function -- make_population_list
        make a list of populations from the NeighbourhoodPopulation
        objects in the given lists
    Parameters:
        neighbourhood_population_object_list -- a list of NeighbourhoodPopulation objects
        age_group -- a string referring to a specific age group
    Return:
        return a list of integers that are populations for neighbourhoods
    Raises:
        TypeError -- when the first argument is not a list
        TypeError -- when the second argument is not a string
        ValueError -- when the second argumnet is not one of the default ones
        ValueError -- when given list's elements are not all NeighbourhoodPopulation objects
    '''
    if not isinstance(neighbourhood_population_object_list, list):
        raise TypeError("children_population_object_list for"\
                        " make_population_list() must be a list.")

    if not isinstance(age_group, str):
        raise TypeError("age_group for make_population_list()"\
                        " must be a string.")

    if age_group not in [AGE_GROUP_0_14, AGE_GROUP_15_64,
                         AGE_GROUP_65_ABOVE, AGE_GROUP_ALL]:
        raise ValueError("invalid age group")

    for i in neighbourhood_population_object_list:
        if not isinstance(i, NeighbourhoodPopulation):
            raise ValueError("the argument for make_population_list() "\
                             "must be a list of NeighbourhoodPopulation objects.")

    population_list = []
    
    if age_group == AGE_GROUP_0_14:
        for i in neighbourhood_population_object_list:
            population_list.append(i.population_0_14)
    elif age_group == AGE_GROUP_15_64:
        for i in neighbourhood_population_object_list:
            population_list.append(i.population_15_64)
    elif age_group == AGE_GROUP_65_ABOVE:
        for i in neighbourhood_population_object_list:
            population_list.append(i.population_65_above)
    else:
        for i in neighbourhood_population_object_list:
            population_list.append(i.population_total)

    return population_list

def make_park_area_dictionary(park_object_list):
    '''
    Function -- make_park_area_dictionary
        make a dictionary with neighbourhood names as keys and 
        corresponding park areas as values
    Parameters:
        park_object_list -- a list of Park objects
    Return:
        return a dictionary as described above
    Raises:
        TypeError -- when the argument is not a list
        ValueError -- when given list's elements are not all Park objects
    '''
    if not isinstance(park_object_list, list):
        raise TypeError("the argument for make_park_area_dictionary()"\
                        " must be a list.")
    
    for i in park_object_list:
        if not isinstance(i, Park):
            raise ValueError("the argument for make_park_area_dictionary() "\
                             "must be a list of Park objects.")

    park_area_dictionary = {}

    for i in park_object_list:

        if i.neighbourhood not in park_area_dictionary:
            park_area_dictionary[i.neighbourhood] = i.area_in_hectare
        else:
            park_area_dictionary[i.neighbourhood] += i.area_in_hectare

    return park_area_dictionary

def make_park_area_list(neighbourhood_list, park_area_dictionary):
    '''
    Function -- make_park_area_list
        make a list of park area numbers from the Park objects in 
        the given lists
    Parameters:
        neighbourhood_list -- a list of neighbourhood names
        park_area_dictionary -- a dictionary with neighbourhood names
        as keys and corresponding park area numbers as values
    Return:
        return a list of floats that are neighbourhoods' areas
    Raises:
        TypeError -- when neighbourhood_list is not a list
        TypeError -- when park_area_dictionary is not a dictionary
    '''
    if not isinstance(neighbourhood_list, list):
        raise TypeError("neighbourhood_list for make_park_area_list()"\
                        " must be a list")
    
    if not isinstance(park_area_dictionary, dict):
        raise TypeError("park_area_dictionary for make_park_area_list()"\
                        " must be a dictionary")

    park_area_list = []

    for i in neighbourhood_list:
        park_area_list.append(park_area_dictionary[i])

    return park_area_list

def make_area_per_thousand_list(population_list, park_area_list):
    '''
    Function -- make_area_per_thousand_list
        make a list of park area numbers per 1000 people of
        a specific age group of each neighbourhood
    Parameters:
        population_list -- a list of integers
        park_area_list -- a list of floats
    Return:
        return a list as described above
    Raises:
        TypeError -- when any of the arguments is not a list
    '''
    for i in [population_list, park_area_list]:
        if not isinstance(i, list):
            raise TypeError("the arguments for make_area_per_thousand_list()"\
                            " must be lists")
    
    area_per_thousand_list = []

    for i in range(len(population_list)):
        area_per_capita = park_area_list[i] / population_list[i]
        area_per_thousand_rounded = round(area_per_capita * UNIT_FOR_AVERAGING,
                                          ROUNDED_DECIMAL)

        area_per_thousand_list.append(area_per_thousand_rounded)

    return area_per_thousand_list

def make_result_data_frame(neighbourhood_list,
                           park_area_list,
                           population_list_0_14,
                           park_area_per_thousand_list_0_14,
                           population_list_15_64,
                           park_area_per_thousand_list_15_64,
                           population_list_65_above,
                           park_area_per_thousand_list_65_above,
                           population_list_total,
                           park_area_per_thousand_list_total,
                           headers):
    '''
    Function -- make_result_data_frame
        make a dataframe that contains neighbourhood names, total park areas,
        populations, and park areas per 1000 for each age group
    Parameters:
        neighbourhood_list -- a list of neighbourhood names
        park_area_list -- a list of floats
        population_list_0_14 -- a list of integers
        area_per_thousand_list_0_14 -- a list of floats
        population_list_15_64 -- a list of integers
        area_per_thousand_list_15_64 -- a list of floats
        population_list_65_above -- a list of integers
        area_per_thousand_list_65_above -- a list of floats
        population_list_total -- a list of integers
        area_per_thousand_list_total -- a list of floats
        headers -- a list of strings
    Return:
        return a pandas.DataFrame object as described above
    Raises:
        TypeError -- when any of the arguments is not a list
    '''
    for i in [neighbourhood_list, park_area_list,
              population_list_0_14, park_area_per_thousand_list_0_14,
              population_list_15_64, park_area_per_thousand_list_15_64,
              population_list_65_above, park_area_per_thousand_list_65_above,
              population_list_total, park_area_per_thousand_list_total,
              headers]:
              if not isinstance(i, list):
                raise TypeError("arguments for make_result_data_frame()"\
                                " must be lists")
    
    data = (neighbourhood_list, park_area_list,
            population_list_0_14, park_area_per_thousand_list_0_14,
            population_list_15_64, park_area_per_thousand_list_15_64,
            population_list_65_above, park_area_per_thousand_list_65_above,
            population_list_total, park_area_per_thousand_list_total)

    data_dictionary = dict(zip(headers, data))

    data_frame = pd.DataFrame(data_dictionary)
    data_frame = data_frame.set_index(headers[0])

    return data_frame