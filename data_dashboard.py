'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
data_dashboard.py
Fengting Tang
'''


from src.data_cleaning_functions import *
from src.data_analysis_functions import *
from src.interface_app_class import *

#census data constants
CENSUS_URL = "https://webtransfer.vancouver.ca/opendata/csv/"\
             "CensusLocalAreaProfiles2016.csv"
CENSUS_USEFUL_LINES_FROM = [5, 7, 11, 22]
CENSUS_USEFUL_LINES_TO = [5, 7, 11, 22]
CENSUS_USEFUL_COLUMNS_FROM = [3]
CENSUS_USEFUL_COLUMNS_TO = [24]

#park data constants
PARKS_URL = "https://opendata.vancouver.ca/explore/dataset/"\
            "parks/download/?format=csv&timezone=America/"\
            "Los_Angeles&lang=en&use_labels_for_header=true"\
            "&csv_separator=%3B"
PARKS_USEFUL_LINES_FROM = [2]
PARKS_USEFUL_LINES_TO = [217]
PARKS_USEFUL_COLUMNS_FROM = [2, 12, 14]
PARKS_USEFUL_COLUMNS_TO = [2, 12, 14]

def main():

    try:
        #get census data
        census_response = get_response(CENSUS_URL)
        census_lines = get_lines(census_response)

        #clean census data
        census_useful_lines = extract_lines(census_lines, 
                                            CENSUS_USEFUL_LINES_FROM,
                                            CENSUS_USEFUL_LINES_TO)
        census_columns_split = split_columns(census_useful_lines, ",")
        census_data_useful = extract_columns(census_columns_split,
                                         CENSUS_USEFUL_COLUMNS_FROM,
                                         CENSUS_USEFUL_COLUMNS_TO)
        census_data_cleaned = convert_string_to_number(census_data_useful)

        #create NeighbourhoodPopulation objects list using the cleaned census data
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        
        #get park data
        park_response = get_response(PARKS_URL)
        park_lines = get_lines(park_response)

        #clean park data
        park_useful_lines = extract_lines(park_lines, 
                                            PARKS_USEFUL_LINES_FROM,
                                            PARKS_USEFUL_LINES_TO)
        park_columns_split = split_columns(park_useful_lines, ";")
        park_data_useful = extract_columns(park_columns_split,
                                        PARKS_USEFUL_COLUMNS_FROM,
                                        PARKS_USEFUL_COLUMNS_TO)
        park_data_cleaned = convert_string_to_number(park_data_useful)
        
        #create Park objects list using the cleaned park data
        park_object_list = make_park_object_list(park_data_cleaned)

        #analyze the objects and create lists that will be the columns of future dataframe
        neighbourhood_list = make_neighbourhood_list(neighbourhood_population_object_list)
        park_area_dictionary = make_park_area_dictionary(park_object_list)
        park_area_list = make_park_area_list(neighbourhood_list, park_area_dictionary)
        population_list_0_14 = make_population_list(neighbourhood_population_object_list,
                                                    AGE_GROUP_0_14)
        park_area_per_thousand_list_0_14 = make_area_per_thousand_list(population_list_0_14,
                                                         park_area_list)
        population_list_15_64 = make_population_list(neighbourhood_population_object_list,
                                                    AGE_GROUP_15_64)
        park_area_per_thousand_list_15_64 = make_area_per_thousand_list(population_list_15_64,
                                                         park_area_list)
        population_list_65_above = make_population_list(neighbourhood_population_object_list,
                                                    AGE_GROUP_65_ABOVE)
        park_area_per_thousand_list_65_above = make_area_per_thousand_list(population_list_65_above,
                                                         park_area_list)
        population_list_total = make_population_list(neighbourhood_population_object_list,
                                                    AGE_GROUP_ALL)
        park_area_per_thousand_list_total = make_area_per_thousand_list(population_list_total,
                                                         park_area_list)
        
        #create the original dataframe which will be changed based on user's choices
        data_frame = make_result_data_frame(neighbourhood_list,
                                            park_area_list,
                                            population_list_0_14,
                                            park_area_per_thousand_list_0_14,
                                            population_list_15_64,
                                            park_area_per_thousand_list_15_64,
                                            population_list_65_above,
                                            park_area_per_thousand_list_65_above,
                                            population_list_total,
                                            park_area_per_thousand_list_total,
                                            HEADERS)

        #launch the interface
        root = Tk()
        interface_app = InterfaceApp(root, data_frame)
        root.mainloop()

    except HTTPError as ex:
        print("\na HTTP error occurred: ", ex)
    except ConnectionError as ex:
        print("\na connection error occurred: ", ex)
    except TypeError as ex:
        print("\na type error occurred: ", ex)
    except ValueError as ex:
        print("\na value error occurred: ", ex)

if __name__ == "__main__":
    main()