'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
test_data_cleaning_functions.py
(move this file to the parent directory before running)
Fengting Tang
'''


import unittest
from src.data_cleaning_functions import *

class testDataCleaningFunctions(unittest.TestCase):
    '''
    Class -- testDataCleaningFunctions
        test functions in data_cleaning_functions.py
    '''

    def test_get_lines_takes_in_list(self):
        with self.assertRaises(TypeError):
            get_lines([])

    def test_get_lines_takes_in_integer(self):
        with self.assertRaises(TypeError):
            get_lines(6)

    def test_get_lines_takes_in_string(self):
        with self.assertRaises(TypeError):
            get_lines("test")

    def test_extract_lines_happy_path(self):
        lines = ["111", "222", "333", "444", "555", "666"]
        lines_from = [2, 4]
        lines_to = [2, 5]
        self.assertEqual(extract_lines(lines, lines_from, lines_to),
                                       ["222", "444", "555"])

    def test_extract_lines_takes_in_string(self):
        lines = "111"
        lines_from = [2, 4]
        lines_to = [2, 5]
        with self.assertRaises(TypeError):
            extract_lines(lines, lines_from, lines_to)

    def test_extract_lines_takes_in_integer(self):
        lines = ["111", "222", "333", "444", "555", "666"]
        lines_from = 2
        lines_to = [2, 5]
        with self.assertRaises(TypeError):
            extract_lines(lines, lines_from, lines_to)
    
    def test_extract_lines_takes_in_dict(self):
        lines = ["111", "222", "333", "444", "555", "666"]
        lines_from = [2, 4]
        lines_to = {}
        with self.assertRaises(TypeError):
            extract_lines(lines, lines_from, lines_to)
    
    def test_extract_lines_takes_in_different_lenght_list(self):
        lines = ["111", "222", "333", "444", "555", "666"]
        lines_from = [2, 4]
        lines_to = [2, 5, 6]
        with self.assertRaises(ValueError):
            extract_lines(lines, lines_from, lines_to)

    def test_split_columns_happy_path(self):
        lines = ["ab,c,def", "g,hi,jk", "lmn,op,q"]
        separator = ","
        self.assertEqual(split_columns(lines, separator),
                         [["ab", "c", "def"],
                          ["g", "hi", "jk"],
                          ["lmn", "op", "q"]])

    def test_split_columns_takes_string_lines(self):
        lines = "ab,c,def"
        separator = ","
        with self.assertRaises(TypeError):
            split_columns(lines, separator)
    
    def test_split_columns_takes_dict_separator(self):
        lines = "ab,c,def"
        separator = {}
        with self.assertRaises(TypeError):
            split_columns(lines, separator)

    def test_extract_columns_happy_path(self):
        lines = [["ab", "c", "def", "g", "hi", "jk"],
                 ["g", "hi", "jk", "lmn", "op", "q"],
                 ["lmn", "op", "q", "ab", "c", "def"]]
        columns_from = [1, 5]
        columns_to = [3, 5]
        self.assertEqual(extract_columns(lines, columns_from, columns_to),
                         [["ab", "c", "def", "hi"],
                          ["g", "hi", "jk", "op"],
                          ["lmn", "op", "q", "c"]])
    
    def test_extract_columns_takes_in_string(self):
        lines = "ab"
        columns_from = [1, 5]
        columns_to = [3, 5]
        with self.assertRaises(TypeError):
            extract_columns(lines, columns_from, columns_to)

    def test_extract_lines_takes_in_integer(self):
        lines = [["ab", "c", "def", "g", "hi", "jk"],
                 ["g", "hi", "jk", "lmn", "op", "q"],
                 ["lmn", "op", "q", "ab", "c", "def"]]
        columns_from = 5
        columns_to = [3, 5]
        with self.assertRaises(TypeError):
            extract_lines(lines, columns_from, columns_to)
    
    def test_extract_lines_takes_in_dict(self):
        lines = [["ab", "c", "def", "g", "hi", "jk"],
                 ["g", "hi", "jk", "lmn", "op", "q"],
                 ["lmn", "op", "q", "ab", "c", "def"]]
        columns_from = [1, 5]
        columns_to = {}
        with self.assertRaises(TypeError):
            extract_lines(lines, columns_from, columns_to)
    
    def test_extract_lines_takes_in_different_lenght_list(self):
        lines = [["ab", "c", "def", "g", "hi", "jk"],
                 ["g", "hi", "jk", "lmn", "op", "q"],
                 ["lmn", "op", "q", "ab", "c", "def"]]
        columns_from = [1, 5, 6]
        columns_to = [3, 5]
        with self.assertRaises(ValueError):
            extract_lines(lines, columns_from, columns_to)

    def test_convert_string_to_number_happy_path(self):
        lines = [["ab", "123", "def", "g", "hi", "jk"],
                 ["g", "hi", "jk", "45.6", "op", "q"],
                 ["lmn", "78", "q", "10.0", "c", "def"]]
        self.assertAlmostEqual(convert_string_to_number(lines),
                        [["ab", 123, "def", "g", "hi", "jk"],
                         ["g", "hi", "jk", 45.6, "op", "q"],
                         ["lmn", 78, "q", 10.0, "c", "def"]])

    def test_convert_string_to_number_takes_in_integer(self):
        lines = 123
        with self.assertRaises(TypeError):
            convert_string_to_number(lines)
    
    def test_convert_string_to_number_takes_in_string(self):
        lines = "123"
        with self.assertRaises(TypeError):
            convert_string_to_number(lines)
    
    def test_convert_string_to_number_takes_in_dict(self):
        lines = {}
        with self.assertRaises(TypeError):
            convert_string_to_number(lines)

def main():
    unittest.main(verbosity=3)

if __name__ == "__main__":
    main()