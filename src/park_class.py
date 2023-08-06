'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
park_class.py
Fengting Tang
'''


class Park:
    '''
    Class -- Park
        data sets that each contains a park name, a neighbourhood name,
        and a corresponding area number
    Attributes:
        park_name -- a string
        neighbourhood -- a string
        area_in_hectare -- a float
    Methods:
        __init__ -- construtor
        validate -- raise errors if any attribute is invalid
        __str__ -- print the object's info
        __eq__ comparing the value of area_in_hectare attribute
    '''
    def __init__(self, park_name, neighbourhood, area_in_hectare):
        '''
        Method -- __init__
            the constructor
        Parameters:
            self -- self
            park_name -- a string
            neighbourhood -- a string
            area_in_hetare -- a float
        Return:
            no return
        Raises:
            TypeError -- when park_name is not a string
            TypeError -- when neighbourhood is not a string
            TypeError -- when area_in_hectare is not a float
        '''
        if not isinstance(park_name, str):
            raise TypeError("park_name for Park() must be a string")
        if not isinstance(neighbourhood, str):
            raise TypeError("neighbourhood for Park() must be a string")
        if not isinstance(area_in_hectare, float):
            raise TypeError("area_in_hectare for Park() must be a float")
        
        self.park_name = park_name
        self.neighbourhood = neighbourhood
        self.area_in_hectare = area_in_hectare

    def validate(self):
        '''
        Method -- validate
            validate a Park object, raise error if
            any attribute is invalid
        Parameters:
            self -- self
        Return:
            no return
        Raises:
            TypeError -- when park_name is not a string
            TypeError -- when neighbourhood is not a string
            TypeError -- when area_in_hectare is not a float
        '''
        if not isinstance(self.park_name, str):
            raise TypeError("invalid Park object, "\
                            "park_name must be a string")
        if not isinstance(self.neighbourhood, str):
            raise TypeError("invalid Park object, "\
                            "neighbourhood must be a string")
        if not isinstance(self.area_in_hectare, float):
            raise TypeError("invalid Park object, "\
                            "area_in_hectare must be a float")

    def __str__(self):
        '''
        Method -- __str__
            Return a string of the object's info
        Parameters:
            self -- self
        Return:
            Return a string of the object's info
        Raises:
            TypeError -- when park_name is not a string
            TypeError -- when neighbourhood is not a string
            TypeError -- when area_in_hectare is not a float
        '''
        self.validate()

        output = (str(self.park_name) + " is located in " +
                  str(self.neighbourhood) + ", and covers an area of " +
                  str(self.area_in_hectare) + " hectares.")

        return output

    def __eq__(self, other):
        '''
        Method -- __eq__
            return the result of comparing the value of area_in_hectare
            attribute
        Parameters:
            self -- self
            other -- a Park, integer or float
        Return:
            return the result in boolean
        Raises:
            TypeError -- when eigher object is invlaid
        '''
        self.validate()

        if isinstance(other, Park):
            other.validate()
            return self.area_in_hectare == other.area_in_hectare

        else:
            return self.area_in_hectare == other