'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
test_neighbourhood_population_class.py
(move this file to the parent directory before running)
Fengting Tang
'''


import unittest
from src.neighbourhood_population_class import *

class testNeighbourhoodPopulationClass(unittest.TestCase):
    '''
    Class -- testNeighbourhoodPopulationClass
        test the class of NeighbourhoodPopulation
    '''
    
    @classmethod
    def setUpClass(self):
        self.valid_instance = NeighbourhoodPopulation("neighbourhood_a",
                                                      100,
                                                      200,
                                                      300,
                                                      600)

        self.valid_instance_2 = NeighbourhoodPopulation("neighbourhood_b",
                                                      300,
                                                      200,
                                                      100,
                                                      600)

        self.valid_instance_3 = NeighbourhoodPopulation("neighbourhood_c",
                                                      300,
                                                      200,
                                                      200,
                                                      700)

        self.invalid_instance_with_integer_neibourhood_name = NeighbourhoodPopulation("neighbourhood_a",
                                                                                      100,
                                                                                      200,
                                                                                      300,
                                                                                      600)
        self.invalid_instance_with_integer_neibourhood_name.neighbourhood = 123

        self.invalid_instance_with_string_population = NeighbourhoodPopulation("neighbourhood_a",
                                                                                      100,
                                                                                      200,
                                                                                      300,
                                                                                      600)
        self.invalid_instance_with_string_population.population_15_64 = "200"

    def test_init_happy_path(self):
        instance = NeighbourhoodPopulation("neighbourhood_a",
                                           100,
                                           200,
                                           300,
                                           600)
        self.assertTrue(isinstance(instance, NeighbourhoodPopulation))
        self.assertEqual(instance.neighbourhood,
                         "neighbourhood_a")
        self.assertEqual(instance.population_0_14,
                         100)
        self.assertEqual(instance.population_15_64,
                         200)
        self.assertEqual(instance.population_65_above,
                         300)
        self.assertEqual(instance.population_total,
                         600)
    
    def test_init_integer_neighbourhood_name(self):
        with self.assertRaises(TypeError):
            NeighbourhoodPopulation(123, 100, 200, 300, 600)
    
    def test_init_string_population(self):
        with self.assertRaises(TypeError):
            NeighbourhoodPopulation("neighbourhood_a",
                                    100,
                                    "200",
                                    300,
                                    600)
    
    def test_validate_valid_instance(self):
        self.assertTrue(self.valid_instance.validate()==None)

    def test_validate_instance_with_integer_neighbourhood_name(self):
        with self.assertRaises(TypeError):
            self.invalid_instance_with_integer_neibourhood_name.validate()

    def test_validate_instance_with_string_population(self):
        with self.assertRaises(TypeError):
            self.invalid_instance_with_string_population.validate()

    def test_str_happy_path(self):
        self.assertEqual(str(self.valid_instance),
                         "The population of neighbourhood_a is: 600")
    
    def test_str_invalid_instance(self):
        with self.assertRaises(TypeError):
            str(self.invalid_instance_with_string_population)

    def test_eq_happy_path_with_another_instance_equal(self):
        self.assertEqual(self.valid_instance,
                         self.valid_instance_2)
    
    def test_eq_happy_path_with_another_instance_inequal(self):
        self.assertNotEqual(self.valid_instance,
                         self.valid_instance_3)

    def test_eq_happy_path_with_integer_equal(self):
        self.assertEqual(self.valid_instance,
                         600)

    def test_eq_happy_path_with_integer_inequal(self):
        self.assertNotEqual(self.valid_instance,
                         700)

    def test_eq_happy_path_with_float_equal(self):
        self.assertEqual(self.valid_instance,
                         600.0)

    def test_eq_happy_path_with_float_inequal(self):
        self.assertNotEqual(self.valid_instance,
                         700.0)

    def test_eq_with_invalid_instance(self):
        with self.assertRaises(TypeError):
            self.valid_instance == self.invalid_instance_with_string_population

def main():
    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()