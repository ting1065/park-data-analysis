'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
data_cleaning_functions.py
Fengting Tang
'''


import requests
from requests.exceptions import HTTPError, ConnectionError

def get_response(file_url):
    '''
    Function -- get_response
        access the content of the given url, and save as a Response object
    Parameters:
        file_url -- a string
    Return:
        return the Response object
    Exceptions:
        HTTPError -- when a HTTP error occurred, print message
        ConnectionError -- when a connection occurred, print message
    '''
    try:
        file_response = requests.get(file_url)
        
        return file_response

    except HTTPError as ex:
        print(f"\na HTTP error occurred while opening {file_url}: "\
              f"{ex}")
    except ConnectionError as ex:
        print(f"\na connection error occurred while opening {file_url}: "\
              f"{ex}")

def get_lines(file_response):
    '''
    Functions -- get_lines
        convert a Response object to a list of strings
    Parameters:
        file_response -- a request.Response object
    Return:
        return a list of strings, each element corresponds to one row of the csv
    Raises:
        TypeError -- when the given argument is not a Response object 
    '''
    if not isinstance(file_response, requests.Response):
        raise TypeError("The argument for get_lines()"\
                        " must be a Response object.")

    file_content = file_response.text

    lines = file_content.splitlines()

    return lines

def extract_lines(lines, lines_from, lines_to):
    '''
    Function -- extract_lines
        extract the wanted strings from a list of strings, and put
        them in a new list.
    Parameters:
        lines -- a list of strings
        lines_from -- a list of integers, which represent start points
        lines_to -- a list of integers, which represent end points
    Return:
        return a list of wanted strings(lines)
    Raises:
        TypeError -- when any one of the arguments is not a list
        ValueError -- when the lengths of lines_from and lines_to are different
    '''
    for i in [lines, lines_from, lines_to]:
        if not isinstance(i, list):
            raise TypeError("The arguments for extract_lines() "\
                            "must be lists.")

    if len(lines_from) != len(lines_to):
        raise ValueError("lines_from and lines_to for extract_lines() "\
                         "must have the same length")

    new_lines = []

    for i in range(len(lines_from)):
        wanted_lines = lines[lines_from[i] - 1 : lines_to[i]]
        for n in wanted_lines:
            new_lines.append(n)

    return new_lines

def split_columns(lines, separator):
    '''
    Function -- split_columns
        split a list of strings into a list of sub-lists of strings
    Parameters:
        lines -- a list of strings
        separator --  a string, used to separate the elements of lines
    Return:
        return the a list of lists, each sub-list is a list of strings.
        the Nth element of the Mth sub-list represents row N, colomn M
    Raises:
        TypeError -- when lines is not a list
        TypeError -- when separator is not a string
    '''
    if not isinstance(lines, list):
        raise TypeError("lines for split_column() must be a list")
    
    if not isinstance(separator, str):
        raise TypeError("separator for split_columns() must be a string")

    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(separator)

    return lines

def extract_columns(lines, columns_from, columns_to):
    '''
    Function -- extract_columns
        create a new list of lists, where each sub-list only contains
        the wanted strings of the corresponding  original sub-list
    Parameters:
        lines -- a list of lists of strings
        columns_from -- a list of integers, which represent start points
        columns_to -- a list of integers, which represent end points
    Return:
        return a list of lists as decribed above
    Raises:
        TypeError -- when any of the arguments is not a list
        ValueError -- when the lengths of columns_from and columns_to
                      are not equal
    '''
    for i in [lines, columns_from, columns_to]:
        if not isinstance(i, list):
            raise TypeError("The arguments for extract_columns() "\
                            "must be lists.")

    if len(columns_from) != len(columns_to):
        raise ValueError("columns_from and columns_to for extract_lines() "\
                         "must have the same length")

    new_lines = []

    for i in lines:

        single_new_line = []

        for n in range(len(columns_from)):
            wanted_columns = i[columns_from[n]-1 : columns_to[n]]
            for m in wanted_columns:
                m = m.strip()
                single_new_line.append(m)

        new_lines.append(single_new_line)

    return new_lines

def convert_string_to_number(lines):
    '''
    Function -- convert_string_to_number
        convert the numerical elements of the given list's
        sub-lists onto floats
    Parameters:
        lines -- a list of lists of strings
    Return:
        return a list of list of strings and floats
    Raises;
        TypeError -- when lines is not a list
    '''
    if not isinstance(lines, list):
        raise TypeError("the argument for convert_string_to_number()"\
                        " must be a list")

    for i in range(len(lines)):
        for n in range(len(lines[i])):
            if lines[i][n].isnumeric():
                lines[i][n] = int(lines[i][n])
            elif lines[i][n].replace(".", "").isnumeric():
                lines[i][n] = float(lines[i][n])

    return lines