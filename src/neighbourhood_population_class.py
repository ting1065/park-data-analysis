'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
neighbourhood_population_class.py
Fengting Tang
'''


class NeighbourhoodPopulation:
    '''
    Class -- NeighbourhoodPopulation
        data sets that each contains a neighbourhood name and
        populations for 4 kinds of age groups
    Attributes:
        neighbourhood -- a string
        population_0_14 -- an integer, population of aged 0-14
        population_15_64 -- an integer, population of aged 15-64
        population_65_above -- an integer, population of aged 65 and above
        population_total -- an integer, population of all age groups
    Methods:
        __init__ -- construtor
        validate -- raise errors if either attribute is invalid
        __str__ -- print the object's info
        __eq__ comparing the value of total population attribute
    '''

    def __init__(self, neighbourhood, population_0_14, population_15_64,
                 population_65_above, population_total):
        '''
        Method -- __init__
            the constructor
        Parameters:
            self -- self
            neighbourhood -- a string
            population_0_14 -- an integer
            population_15_64 -- an integer
            population_65_above -- an integer
            population_total -- an integer
        Return:
            no return
        Raises:
            TypeError -- when neighbourhood is not a string
            TypeError -- when any population data is not an integer
        '''
        if not isinstance(neighbourhood, str):
            raise TypeError("neighbourhood for NeighbourhoodPopulation() "\
                             "must be a string")
        for i in [population_0_14, population_15_64, population_65_above]:
            if not isinstance(i, int):
                raise TypeError("populations for NeighbourhoodPopulation() "\
                                "must be integers")
        
        self.neighbourhood = neighbourhood
        self.population_0_14 = population_0_14
        self.population_15_64 = population_15_64
        self.population_65_above = population_65_above
        self.population_total = population_total
    
    def validate(self):
        '''
        Method -- validate
            validate a NeighbourhoodPopulation object, raise error if
            any attribute is invalid
        Parameters:
            self -- self
        Return:
            no return
        Raises:
            TypeError -- when neighbourhood is not a string
            TypeError -- when any of population data is not an integer
        '''
        if not isinstance(self.neighbourhood, str):
            raise TypeError("invalid NeighbourhoodPopulation object, "\
                            "neighbourhood must be a string")
        for i in [self.population_0_14, self.population_15_64,
                  self.population_65_above, self.population_total]:
            if not isinstance(i, int):
                raise TypeError("invalid NeighbourhoodPopulation object, "\
                                "populations must be integers")

    def __str__(self):
        '''
        Method -- __str__
            Return a string of the object's info
        Parameters:
            self -- self
        Return:
            Return a string of the object's info
        Raises:
            TypeError -- the object is invalid
        '''
        self.validate()

        output = ("The population of " +
                  str(self.neighbourhood) +
                  " is: " + str(self.population_total))
        
        return output

    def __eq__(self, other):
        '''
        Method -- __eq__
            return the result of comparing the value of the total
            population attribute
        Parameters:
            self -- self
            other -- a NeighbourhoodPopulation, integer or float
        Return:
            return the result in boolean
        Raises:
            TypeError -- when either object is invalid
        '''
        self.validate()

        if isinstance(other, NeighbourhoodPopulation):
            other.validate()
            return self.population_total == other.population_total

        else:
            return self.population_total == other