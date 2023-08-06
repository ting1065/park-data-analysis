'''
Park Data Analysis
Retrieve, clean, analyze, and visualize data about parks and population in Vancouver
interface_app_class.py
Fengting Tang
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from src.data_analysis_functions import AGE_GROUP_0_14, AGE_GROUP_15_64, AGE_GROUP_65_ABOVE, AGE_GROUP_ALL

#constants for the window and frames
WINDOW_TITLE = "5001 Final Project -- Fengting Tang"
WINDOW_SIZE = "310x400"
FRAME_TITLE_BAR_GRAPH = "Park Area Per Capita"
FRAME_TITLE_PIE_GRAPH = "Demographic Structure"
WINDOW_LEVEL_PAD_SIZE = 10
FRAME_LEVEL_PAD_SIZE = 2
FRAME_HEIGHT = 300
FRAME_WIDTH = 600
WINDOW_CENTERING_COMMAND_STRING = 'tk::PlaceWindow . center'

#constants for widgets
COMBOBOX_LABELS = ["choose an age group", "choose a range to display",
                   "choose a sorting method", "choose a neighbourhood"]
BUTTON_TEXTS = ["show me the bars!", "show me the pie!"]
AGE_GROUPS = [AGE_GROUP_0_14, AGE_GROUP_15_64, AGE_GROUP_65_ABOVE, AGE_GROUP_ALL]
DISPLAY_RANGE = ["All Neighbourhoods", "Top 3", "Bottom 3"]
SORTING_METHODS = ["Ascending", "Descending"]
NEIGHBOURHOODS = ["Arbutus-Ridge", "Downtown", "Dunbar-Southlands", "Fairview", 
                  "Grandview-Woodland", "Hastings-Sunrise", "Kensington-Cedar Cottage", 
                  "Kerrisdale", "Killarney", "Kitsilano", "Marpole", "Mount Pleasant", 
                  "Oakridge", "Renfrew-Collingwood", "Riley Park", "Shaughnessy", 
                  "South Cambie", "Strathcona", "Sunset", "Victoria-Fraserview",
                  "West End", "West Point Grey"] 
MESSAGE_BOX_TITLE = "oops!"
MESSAGE_BOX_MESSAGES = ["You need to choose an age group.",
                        "You need to choose a display range.",
                        "You need to choose a sorting method.",
                        "You need to choose a neighbourhood."]

#constants for dataframes
HEADERS = ["neighbourhood", "park area in hectare",
           "population of aged 0-14", "park area per 1000 people aged 0-14",
           "population of aged 15-64", "park area per 1000 people aged 15-64",
           "population of aged 65 and above", "park area per 1000 people aged 65 and above",
           "population in total", "park area per 1000 people in total"]

#constants for output graph
GRAPH_SIZE = (10, 10)
BAR_GRAPH_KIND = "bar"
BAR_GRAPH_YLABEL = "unit: hectare"
PIE_GRAPH_KIND = "pie"
PIE_GRAPH_AUTOPCT_FORMAT = '%1.2f%%'
PIE_GRAPH_YLABEL_COORDINATE_X = 0.5
PIE_GRAPH_YLABEL_COORDINATE_Y = 0
PIE_GRAPH_YLABEL_ROTATION = 0


class InterfaceApp:
    '''
    Class -- InterfaceApp
        An interface for user to change the original dataframe and visualize the results.
    Attributes:
        data_frame -- a pandas dataframe, the original one
        user_choice_age_group -- a StringVar for user to determine the value
        user_choice_display_range -- a StringVar for user to determine the value
        user_choice_sorting_method -- a StringVar for user to determine the value
        user_choice_neighbourhood -- a StringVar for user to determine the value
    Methods:
        __init__ --  constructor
        get_new_data_frame_for_bar_graph -- create a new dataframe for bar graph plotting
        make_bar_graph_from_data_frame -- visualize a dataframe created by get_new_data_frame_for_bar_graph
        get_new_data_fame_for_pie_graph -- create a new dataframe for pie graph plotting
        make_pie_graph_from_data_frame -- visualize a dataframe created by get_new_data_fame_for_pie_graph
    '''

    def __init__(self, master, data_frame):
        '''
        Method -- __init__
            the constructor
        Parameters:
            self -- self
            master -- a Tk object
            data_frame --  a pandas.DataFrame object
        Return:
            no return
        Raises:
            TypeError -- when master is not a TK object
            TypeError -- when data_frame is not a pandas.DataFrame object
        '''
        if not isinstance(master, Tk):
            raise TypeError("master parameter for InterfaceApp must be an Tk object")
        if not isinstance(data_frame, pd.DataFrame):
            raise TypeError("data_frame parameter for InterfaceApp must be an pandas.DataFrame object")
        
        self.data_frame = data_frame
        self.user_choice_age_group = StringVar()
        self.user_choice_display_range = StringVar()
        self.user_choice_sorting_method = StringVar()
        self.user_choice_neighbourhood = StringVar()
        
        #configure the window
        master.title(WINDOW_TITLE)
        master.geometry(WINDOW_SIZE)
        master.resizable(False, False)
        
        #configure labels and frames on the window
        ttk.Label(master, text=FRAME_TITLE_BAR_GRAPH).pack(padx=WINDOW_LEVEL_PAD_SIZE,
                                                     pady=WINDOW_LEVEL_PAD_SIZE)
        park_area_frame = ttk.Frame(master, height=FRAME_HEIGHT,
                                    width=FRAME_WIDTH, relief=RIDGE)
        park_area_frame.pack(padx=WINDOW_LEVEL_PAD_SIZE, pady=WINDOW_LEVEL_PAD_SIZE)
        ttk.Label(master, text=FRAME_TITLE_PIE_GRAPH).pack(padx=WINDOW_LEVEL_PAD_SIZE,
                                                     pady=WINDOW_LEVEL_PAD_SIZE)
        demographic_structure_frame = ttk.Frame(master, height=FRAME_HEIGHT,
                                                width=FRAME_WIDTH, relief=RIDGE)
        demographic_structure_frame.pack(padx=WINDOW_LEVEL_PAD_SIZE,
                                         pady=WINDOW_LEVEL_PAD_SIZE)
        
        #configure the widgets in the first frame
        ttk.Label(park_area_frame, text=COMBOBOX_LABELS[0]).pack(padx=FRAME_LEVEL_PAD_SIZE,
                                                                 pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Combobox(park_area_frame,
                     textvariable=self.user_choice_age_group,
                     values=AGE_GROUPS).pack(padx=FRAME_LEVEL_PAD_SIZE,
                                             pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Label(park_area_frame, text=COMBOBOX_LABELS[1]).pack(padx=FRAME_LEVEL_PAD_SIZE,
                                                                 pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Combobox(park_area_frame,
                     textvariable=self.user_choice_display_range,
                     values=DISPLAY_RANGE).pack(padx=FRAME_LEVEL_PAD_SIZE, pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Label(park_area_frame, text=COMBOBOX_LABELS[2]).pack(padx=FRAME_LEVEL_PAD_SIZE,
                                                                 pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Combobox(park_area_frame,
                     textvariable=self.user_choice_sorting_method,
                     values=SORTING_METHODS).pack(padx=FRAME_LEVEL_PAD_SIZE, pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Button(park_area_frame,
                   command=self.plot_bar_graph_from_new_data_frame,
                   text=BUTTON_TEXTS[0]).pack(padx=FRAME_LEVEL_PAD_SIZE, pady=FRAME_LEVEL_PAD_SIZE)
        
        #configure the widgets in the second frame
        ttk.Label(demographic_structure_frame, text=COMBOBOX_LABELS[3]).pack(padx=FRAME_LEVEL_PAD_SIZE,
                                                                             pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Combobox(demographic_structure_frame,
                     textvariable=self.user_choice_neighbourhood,
                     values=NEIGHBOURHOODS).pack(padx=FRAME_LEVEL_PAD_SIZE, pady=FRAME_LEVEL_PAD_SIZE)
        ttk.Button(demographic_structure_frame,
                   command=self.plot_pie_graph_from_new_data_frame,
                   text=BUTTON_TEXTS[1]).pack(padx=FRAME_LEVEL_PAD_SIZE, pady=FRAME_LEVEL_PAD_SIZE)
        
        #make the window as centered as possible
        master.eval(WINDOW_CENTERING_COMMAND_STRING)
    
    def make_new_data_frame_for_bar_graph(self):
        '''
        Method -- make_new_data_frame_for_bar_graph
            create a new dataframe, which only contains the neighbourhood
            columns and a park area per capita column for a specific age
            group, for bar graph plotting
        Parameters:
            self -- self
        Return:
            Return None when user misses options, otherwise return
            a revised dataframe according to user's choices
        Raises:
            TypeError -- when self.data_frame is not a dataframe 
        '''
        if not isinstance(self.data_frame, pd.DataFrame):
            raise TypeError("self.data_frame must be a pandas.DataFrame object")
        
        #get user's choices
        age_group_choice = self.user_choice_age_group.get()
        display_range_choice = self.user_choice_display_range.get()
        sorting_method_choice = self.user_choice_sorting_method.get()

        #change the dataframe based on the age group chosen by the user
        if age_group_choice == AGE_GROUP_0_14:
            new_data_frame = self.data_frame.loc[:, [HEADERS[3]]]
            new_data_frame = new_data_frame.sort_values(by=HEADERS[3])
        elif age_group_choice == AGE_GROUP_15_64:
            new_data_frame = self.data_frame.loc[:, [HEADERS[5]]]
            new_data_frame = new_data_frame.sort_values(by=HEADERS[5])
        elif age_group_choice == AGE_GROUP_65_ABOVE:
            new_data_frame = self.data_frame.loc[:, [HEADERS[7]]]
            new_data_frame = new_data_frame.sort_values(by=HEADERS[7])
        elif age_group_choice == AGE_GROUP_ALL:
            new_data_frame = self.data_frame.loc[:, [HEADERS[9]]]
            new_data_frame = new_data_frame.sort_values(by=HEADERS[9])
        else:
            messagebox.showinfo(title=MESSAGE_BOX_TITLE,
                                message=MESSAGE_BOX_MESSAGES[0])
            return

        #change the dataframe base on the display range chosen by the user
        if display_range_choice == DISPLAY_RANGE[0]:
            None
        elif display_range_choice == DISPLAY_RANGE[1]:
            new_data_frame = new_data_frame[-3:]
        elif display_range_choice == DISPLAY_RANGE[2]:
            new_data_frame = new_data_frame[:3]
        else:
            messagebox.showinfo(title=MESSAGE_BOX_TITLE,
                                message=MESSAGE_BOX_MESSAGES[1])
            return
        
        #change the dataframe base on the sorting method chosen by the user
        if sorting_method_choice == SORTING_METHODS[0]:
            None
        elif sorting_method_choice == SORTING_METHODS[1]:
            new_data_frame = new_data_frame. sort_values(by=new_data_frame.columns[0],
                                                         ascending=False)
        else:
            messagebox.showinfo(title=MESSAGE_BOX_TITLE,
                                message=MESSAGE_BOX_MESSAGES[2])
            return

        return new_data_frame

    def plot_bar_graph_from_new_data_frame(self):
        '''
        Method -- plot_bar_graph_from_new_data_frame
            visualize a dataframe created by get_new_data_frame_for_bar_graph
        Parameters:
            self -- self
        Return:
            return None if it fails to create a new dataframe
            because of missing user choices
        Output:
            a bar graph
        '''
        new_data_frame = self.make_new_data_frame_for_bar_graph()

        if isinstance(new_data_frame, type(None)):
            return
        else:
            fig, ax = plt.subplots()
            new_data_frame.plot(kind=BAR_GRAPH_KIND, use_index=True,
                                title=FRAME_TITLE_BAR_GRAPH,
                                figsize=GRAPH_SIZE, ax=ax)
            ax.set_ylabel(BAR_GRAPH_YLABEL)
            fig.autofmt_xdate()
            plt.show()
    
    def make_new_data_frame_for_pie_graph(self):
        '''
        Method -- make_new_data_frame_for_pie_graph
            create a new dataframe, which only contains neighbourhood and
            three population columns of one row, for plotting a pie graph
        Parameters:
            self -- self
        Return:
            return None if user misses the option, otherwise return a
            revised dataframe according to user's choices
        Raises:
            TypeError -- when self.data_frame is not a dataframe  
        '''
        if not isinstance(self.data_frame, pd.DataFrame):
            raise TypeError("self.data_frame must be a pandas.DataFrame object")

        if len(self.user_choice_neighbourhood.get()) == 0:
            messagebox.showinfo(title=MESSAGE_BOX_TITLE, message=MESSAGE_BOX_MESSAGES[3])
            return
        else:
            neighbourhood_choice = self.user_choice_neighbourhood.get()
            new_data_frame = self.data_frame.loc[[neighbourhood_choice],
                                                [HEADERS[2], HEADERS[4], HEADERS[6]]]

        return new_data_frame

    def plot_pie_graph_from_new_data_frame(self):
        '''
        Method -- make_pie_graph_from_new_data_frame
            visualize a dataframe created by get_new_data_frame_for_pie_graph
        Parameters:
            self -- self
        Return:
            return None if it fails to create a new dataframe
            because of missing user choices
        Output:
            a pie graph
        '''
        new_data_frame = self.make_new_data_frame_for_pie_graph()

        if isinstance(new_data_frame, type(None)):
            return
        else:
            fig, ax = plt.subplots()
            new_data_frame.iloc[0].plot(kind=PIE_GRAPH_KIND, title=FRAME_TITLE_PIE_GRAPH,
                                        figsize=GRAPH_SIZE, autopct=PIE_GRAPH_AUTOPCT_FORMAT,
                                        ax=ax)
            ax.yaxis.set_label_coords(PIE_GRAPH_YLABEL_COORDINATE_X,
                                      PIE_GRAPH_YLABEL_COORDINATE_Y)
            ax.yaxis.label.set_rotation(PIE_GRAPH_YLABEL_ROTATION)
            fig.autofmt_xdate()
            plt.show()