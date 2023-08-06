'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
test_park_class.py
(move this file to the parent directory before running)
Fengting Tang
'''


import unittest
from src.park_class import *

class testParkClass(unittest.TestCase):
    '''
    Class -- testParkClass
        test the class of Park
    '''
    
    @classmethod
    def setUpClass(self):
        self.valid_instance = Park("park_a",
                                   "neighbourhood_a",
                                   100.0)

        self.valid_instance_2 = Park("park_b",
                                   "neighbourhood_b",
                                   100.0)

        self.valid_instance_3 = Park("park_c",
                                     "neighbourhood_c",
                                     200.0)

        self.invalid_instance_with_integer_park_name = Park("park_a",
                                                            "neighbourhood_a",
                                                            100.0)
        self.invalid_instance_with_integer_park_name.park_name = 123

        self.invalid_instance_with_string_area = Park("park_a",
                                                      "neighbourhood_a",
                                                      100.0)
        self.invalid_instance_with_string_area.area_in_hectare = "100"

    def test_init_happy_path(self):
        instance = Park("park_a",
                        "neighbourhood_a",
                        100.0)
        self.assertTrue(isinstance(instance, Park))
        self.assertEqual(instance.park_name,
                         "park_a")
        self.assertEqual(instance.neighbourhood,
                         "neighbourhood_a")
        self.assertEqual(instance.area_in_hectare,
                         100.0)
    
    def test_init_integer_park_name(self):
        with self.assertRaises(TypeError):
            Park(123, "neighbourhood_a", 100.0)
    
    def test_init_integer_neighbourhood(self):
        with self.assertRaises(TypeError):
            Park("park_a", 123, 100.0)
    
    def test_init_string_area(self):
        with self.assertRaises(TypeError):
            Park("park_a", "neighbourhood_a", "100.0")
    
    def test_validate_valid_instance(self):
        self.assertTrue(self.valid_instance.validate()==None)

    def test_validate_instance_with_integer_park_name(self):
        with self.assertRaises(TypeError):
            self.invalid_instance_with_integer_park_name.validate()

    def test_validate_instance_with_string_area(self):
        with self.assertRaises(TypeError):
            self.invalid_instance_with_string_area.validate()

    def test_str_happy_path(self):
        self.assertEqual(str(self.valid_instance),
                         "park_a is located in neighbourhood_a, "\
                         "and covers an area of 100.0 hectares.")
    
    def test_str_invalid_instance(self):
        with self.assertRaises(TypeError):
            str(self.invalid_instance_with_string_area)

    def test_eq_happy_path_with_another_instance_equal(self):
        self.assertEqual(self.valid_instance,
                         self.valid_instance_2)
    
    def test_eq_happy_path_with_another_instance_inequal(self):
        self.assertNotEqual(self.valid_instance,
                         self.valid_instance_3)

    def test_eq_happy_path_with_integer_equal(self):
        self.assertEqual(self.valid_instance,
                         100)

    def test_eq_happy_path_with_integer_inequal(self):
        self.assertNotEqual(self.valid_instance,
                         200)

    def test_eq_happy_path_with_float_equal(self):
        self.assertEqual(self.valid_instance,
                         100.0)

    def test_eq_happy_path_with_float_inequal(self):
        self.assertNotEqual(self.valid_instance,
                         200.0)

    def test_eq_with_invalid_instance(self):
        with self.assertRaises(TypeError):
            self.valid_instance == self.invalid_instance_with_string_area

def main():
    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()