'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
test_data_analysis_functions.py
(move this file to the parent directory before running)
Fengting Tang
'''


import unittest
from src.data_analysis_functions import *

class testDataAnalysisFunctions(unittest.TestCase):
    '''
    Class -- testDataAnalysisFunctions
        test functions in data_analysis_functions.py
    '''

    def test_make_neighbourhood_population_object_list_happy_path(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        self.assertTrue(isinstance(neighbourhood_population_object_list, list))
        for i in neighbourhood_population_object_list:
            self.assertTrue(isinstance(i, NeighbourhoodPopulation))
        self.assertEqual(neighbourhood_population_object_list[0].population_0_14, 1)
        self.assertEqual(neighbourhood_population_object_list[1].population_15_64, 5)
        self.assertEqual(neighbourhood_population_object_list[2].population_65_above, 9)
        self.assertEqual(neighbourhood_population_object_list[0].population_total, 12)

    def test_make_neighbourhood_population_object_list_takes_in_string(self):
        census_data_cleaned = "a"
        with self.assertRaises(TypeError):
            make_neighbourhood_population_object_list(census_data_cleaned)
    
    def test_make_neighbourhood_population_object_list_takes_in_integer(self):
        census_data_cleaned = 123
        with self.assertRaises(TypeError):
            make_neighbourhood_population_object_list(census_data_cleaned)
    
    def test_make_neighbourhood_population_object_list_takes_in_dict(self):
        census_data_cleaned = {}
        with self.assertRaises(TypeError):
            make_neighbourhood_population_object_list(census_data_cleaned)

    def test_make_park_object_list_happy_path(self):
        park_data_cleaned = [["park_a", "neighbourhood_a", 100.0],
                             ["park_b", "neighbourhood_b", 200.0],
                             ["park_c", "neighbourhood_c", 300.0]]
        park_object_list = make_park_object_list(park_data_cleaned)
        self.assertTrue(isinstance(park_object_list, list))
        for i in park_object_list:
            self.assertTrue(isinstance(i, Park))
        self.assertEqual(park_object_list[0].park_name, "park_a")
        self.assertEqual(park_object_list[1].neighbourhood, "neighbourhood_b")
        self.assertAlmostEqual(park_object_list[2].area_in_hectare, 300.0)

    def test_make_park_object_list_takes_in_string(self):
        census_data_cleaned = "a"
        with self.assertRaises(TypeError):
            make_park_object_list(census_data_cleaned)
    
    def test_make_park_object_list_takes_in_integer(self):
        census_data_cleaned = 123
        with self.assertRaises(TypeError):
            make_park_object_list(census_data_cleaned)
    
    def test_make_park_object_list_takes_in_dict(self):
        census_data_cleaned = {}
        with self.assertRaises(TypeError):
            make_park_object_list(census_data_cleaned)
    
    def test_make_neighbourhood_list_happy_path(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        self.assertEqual(make_neighbourhood_list(neighbourhood_population_object_list),
                         ["a","b", "c"])

    def test_make_neighbourhood_list_takes_in_string(self):
        with self.assertRaises(TypeError):
            make_neighbourhood_list("a")

    def test_make_neighbourhood_list_takes_in_integer(self):
        with self.assertRaises(TypeError):
           make_neighbourhood_list(666)

    def test_make_neighbourhood_list_takes_in_dict(self):
        with self.assertRaises(TypeError):
            make_neighbourhood_list({})

    def test_make_neighbourhood_list_takes_in_list_of_string(self):
        with self.assertRaises(ValueError):
            make_neighbourhood_list(["a","b", "c"])

    def test_make_population_list_happy_path_0_14(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        population_list_0_14 = make_population_list(neighbourhood_population_object_list,
                                                    AGE_GROUP_0_14)
        self.assertEqual(population_list_0_14, [1, 2, 3])

    def test_make_population_list_happy_path_15_64(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        population_list_15_64 = make_population_list(neighbourhood_population_object_list,
                                                     AGE_GROUP_15_64)
        self.assertEqual(population_list_15_64, [4, 5, 6])
        
    def test_make_population_list_happy_path_65_above(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        population_list_65_above = make_population_list(neighbourhood_population_object_list,
                                                        AGE_GROUP_65_ABOVE)
        self.assertEqual(population_list_65_above, [7, 8, 9])
    
    def test_make_population_list_happy_path_all(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        population_list_all = make_population_list(neighbourhood_population_object_list,
                                                    AGE_GROUP_ALL)
        self.assertEqual(population_list_all, [12, 15, 18])

    def test_make_population_list_first_parameter_takes_in_string(self):
        with self.assertRaises(TypeError):
            make_population_list("neighbourhood_population_object_list",
                                 AGE_GROUP_ALL)

    def test_make_population_list_second_parameter_takes_in_list(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        with self.assertRaises(TypeError):
            make_population_list(neighbourhood_population_object_list,
                                 [])

    def test_make_population_list_second_parameter_takes_in_invalid_string(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        with self.assertRaises(ValueError):
            make_population_list(neighbourhood_population_object_list,
                                 "80 -")
    
    def test_make_population_list_first_parameter_takes_in_invalid_item(self):
        census_data_cleaned = [["a","b", "c"],
                               [1, 2, 3],
                               [4, 5, 6],
                               [7, 8, 9]]
        neighbourhood_population_object_list = make_neighbourhood_population_object_list(census_data_cleaned)
        neighbourhood_population_object_list[1] = "oops"
        with self.assertRaises(ValueError):
            make_population_list(neighbourhood_population_object_list,
                                 AGE_GROUP_ALL)

    def test_make_park_area_dictionary_happy_path(self):
        park_data_cleaned = [["park_a", "neighbourhood_a", 100.0],
                             ["park_b", "neighbourhood_b", 200.0],
                             ["park_c", "neighbourhood_c", 300.0],
                             ["park_d", "neighbourhood_a", 100.0],
                             ["park_e", "neighbourhood_b", 200.0],
                             ["park_f", "neighbourhood_c", 300.0]]
        park_object_list = make_park_object_list(park_data_cleaned)
        park_area_dictionary = make_park_area_dictionary(park_object_list)
        self.assertAlmostEqual(park_area_dictionary,
                         {"neighbourhood_a": 200.0,
                          "neighbourhood_b": 400.0,
                          "neighbourhood_c": 600.0})
    
    def test_make_park_area_dictionary_takes_in_string(self):
        with self.assertRaises(TypeError):
            make_park_area_dictionary("dict")

    def test_make_park_area_dictionary_takes_in_integer(self):
        with self.assertRaises(TypeError):
            make_park_area_dictionary(666)
    
    def test_make_park_area_dictionary_takes_in_dictionary(self):
        with self.assertRaises(TypeError):
            make_park_area_dictionary({})

    def test_make_park_area_dictionary_takes_in_list_with_non_park_object(self):
        park_data_cleaned = [["park_a", "neighbourhood_a", 100.0],
                             ["park_b", "neighbourhood_b", 200.0],
                             ["park_c", "neighbourhood_c", 300.0],
                             ["park_d", "neighbourhood_a", 100.0],
                             ["park_e", "neighbourhood_b", 200.0],
                             ["park_f", "neighbourhood_c", 300.0]]
        park_object_list = make_park_object_list(park_data_cleaned)
        park_object_list[1] = "oops"
        with self.assertRaises(ValueError):
            make_park_area_dictionary(park_object_list)
    
    def test_make_park_area_list_happy_path(self):
        park_area_dictionary = {"neighbourhood_a": 100.0,
                                "neighbourhood_b": 200.0,
                                "neighbourhood_c": 300.0,
                                "neighbourhood_d": 400.0,
                                "neighbourhood_e": 500.0,
                                "neighbourhood_f": 600.0}
        neighbourhood_list = ["neighbourhood_c",
                              "neighbourhood_e",
                              "neighbourhood_a"]
        park_area_list = make_park_area_list(neighbourhood_list, park_area_dictionary)
        self.assertAlmostEqual(park_area_list, [300.0, 500.0, 100.0])

    def test_make_park_area_list_first_parameter_takes_in_string(self):
        park_area_dictionary = {"neighbourhood_a": 100.0,
                                "neighbourhood_b": 200.0}
        neighbourhood_list = "neighbourhood_c"
        with self.assertRaises(TypeError):
            make_park_area_list(neighbourhood_list, park_area_dictionary)
    
    def test_make_park_area_list_second_parameter_takes_in_list(self):
        park_area_dictionary = []
        neighbourhood_list = ["neighbourhood_c",
                              "neighbourhood_e",
                              "neighbourhood_a"]
        with self.assertRaises(TypeError):
            make_park_area_list(neighbourhood_list, park_area_dictionary)

    def test_make_area_per_thousand_list_happy_path(self):
        population_list = [1, 2, 3, 4]
        park_area_list = [1.0, 2.0, 3.0, 4.0]
        area_per_thousand_list = make_area_per_thousand_list(population_list, park_area_list)
        self.assertAlmostEqual(area_per_thousand_list,
                               [1000.0, 1000.0, 1000.0, 1000.0])

    def test_make_area_per_thousand_list_takes_in_string(self):
        population_list = "1, 2, 3, 4"
        park_area_list = [1.0, 2.0, 3.0, 4.0]
        with self.assertRaises(TypeError):
            make_area_per_thousand_list(population_list, park_area_list)
    
    def test_make_area_per_thousand_list_takes_in_dict(self):
        population_list = [1, 2, 3, 4]
        park_area_list = {}
        with self.assertRaises(TypeError):
            make_area_per_thousand_list(population_list, park_area_list)

    def test_make_result_data_frame_happy_path(self):
        neighbourhood_list = ["neighbourhood a",
                              "neighbourhood b",
                              "neighbourhood c",
                              "neighbourhood d"]
        park_area_list = [10.0, 20.0, 30.0, 40.0]
        population_list_0_14 = [1, 1, 1, 1]
        park_area_per_thousand_list_0_14 = [10000.0, 20000.0, 30000.0, 40000.0]
        population_list_15_64 = [2, 2, 2, 2]
        park_area_per_thousand_list_15_64 = [5000.0, 10000.0, 15000.0, 20000.0]
        population_list_65_above = [5, 5, 5, 5]
        park_area_per_thousand_list_65_above = [2000, 4000.0, 6000.0, 8000.0]
        population_list_total = [8, 8, 8, 8]
        park_area_per_thousand_list_total = [1250.0, 2500.0, 3750.0, 5000.0]
        headers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

        result_data_frame = make_result_data_frame(neighbourhood_list,
                                                   park_area_list,
                                                   population_list_0_14,
                                                   park_area_per_thousand_list_0_14,
                                                   population_list_15_64,
                                                   park_area_per_thousand_list_15_64,
                                                   population_list_65_above,
                                                   park_area_per_thousand_list_65_above,
                                                   population_list_total,
                                                   park_area_per_thousand_list_total,
                                                   headers)
        self.assertTrue(isinstance(result_data_frame, pd.DataFrame))
        line_3 = result_data_frame.iloc[2].values.tolist()
        line_3_expected = [30.0, 1, 30000.0, 2,15000.0, 5, 6000.0, 8, 3750.0]
        print(line_3)
        print(line_3_expected)
        self.assertAlmostEqual(line_3, line_3_expected)
        headers_in_dataframe = result_data_frame.columns.values.tolist()
        headers_in_dataframe_expected = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        self.assertEqual(headers_in_dataframe,
                         headers_in_dataframe_expected)
        index_in_dataframe = result_data_frame.index.values.tolist()
        index_in_dataframe_expected = ['neighbourhood a','neighbourhood b',
                                       'neighbourhood c', 'neighbourhood d']
        self.assertEqual(index_in_dataframe,
                         index_in_dataframe_expected)
    
    def test_make_result_data_frame_takes_in_dictionary(self):
        neighbourhood_list = {}
        park_area_list = [10.0, 20.0, 30.0, 40.0]
        population_list_0_14 = [1, 1, 1, 1]
        park_area_per_thousand_list_0_14 = [10000.0, 20000.0, 30000.0, 40000.0]
        population_list_15_64 = [2, 2, 2, 2]
        park_area_per_thousand_list_15_64 = [5000.0, 10000.0, 15000.0, 20000.0]
        population_list_65_above = [5, 5, 5, 5]
        park_area_per_thousand_list_65_above = [2000, 4000.0, 6000.0, 8000.0]
        population_list_total = [8, 8, 8, 8]
        park_area_per_thousand_list_total = [1250.0, 2500.0, 3750.0, 5000.0]
        headers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        with self.assertRaises(TypeError):
            make_result_data_frame(neighbourhood_list,
                                park_area_list,
                                population_list_0_14,
                                park_area_per_thousand_list_0_14,
                                population_list_15_64,
                                park_area_per_thousand_list_15_64,
                                population_list_65_above,
                                park_area_per_thousand_list_65_above,
                                population_list_total,
                                park_area_per_thousand_list_total,
                                headers)

    def test_make_result_data_frame_takes_in_float(self):
        neighbourhood_list = ["neighbourhood a",
                              "neighbourhood b",
                              "neighbourhood c",
                              "neighbourhood d"]
        park_area_list = 10.0
        population_list_0_14 = [1, 1, 1, 1]
        park_area_per_thousand_list_0_14 = [10000.0, 20000.0, 30000.0, 40000.0]
        population_list_15_64 = [2, 2, 2, 2]
        park_area_per_thousand_list_15_64 = [5000.0, 10000.0, 15000.0, 20000.0]
        population_list_65_above = [5, 5, 5, 5]
        park_area_per_thousand_list_65_above = [2000, 4000.0, 6000.0, 8000.0]
        population_list_total = [8, 8, 8, 8]
        park_area_per_thousand_list_total = [1250.0, 2500.0, 3750.0, 5000.0]
        headers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        with self.assertRaises(TypeError):
            make_result_data_frame(neighbourhood_list,
                                park_area_list,
                                population_list_0_14,
                                park_area_per_thousand_list_0_14,
                                population_list_15_64,
                                park_area_per_thousand_list_15_64,
                                population_list_65_above,
                                park_area_per_thousand_list_65_above,
                                population_list_total,
                                park_area_per_thousand_list_total,
                                headers)

    def test_make_result_data_frame_takes_in_integer(self):
        neighbourhood_list = ["neighbourhood a",
                              "neighbourhood b",
                              "neighbourhood c",
                              "neighbourhood d"]
        park_area_list = [10.0, 20.0, 30.0, 40.0]
        population_list_0_14 = 1
        park_area_per_thousand_list_0_14 = [10000.0, 20000.0, 30000.0, 40000.0]
        population_list_15_64 = [2, 2, 2, 2]
        park_area_per_thousand_list_15_64 = [5000.0, 10000.0, 15000.0, 20000.0]
        population_list_65_above = [5, 5, 5, 5]
        park_area_per_thousand_list_65_above = [2000, 4000.0, 6000.0, 8000.0]
        population_list_total = [8, 8, 8, 8]
        park_area_per_thousand_list_total = [1250.0, 2500.0, 3750.0, 5000.0]
        headers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        with self.assertRaises(TypeError):
            make_result_data_frame(neighbourhood_list,
                                park_area_list,
                                population_list_0_14,
                                park_area_per_thousand_list_0_14,
                                population_list_15_64,
                                park_area_per_thousand_list_15_64,
                                population_list_65_above,
                                park_area_per_thousand_list_65_above,
                                population_list_total,
                                park_area_per_thousand_list_total,
                                headers)

        
def main():
    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()