from numpy import test
import pandas as pd
import re
import random
import os
import datetime
import calendar
from pathlib import Path

def clearConsole():
    """clear clonsole 
    """
    command = "clear"
    os.system(command)
    command = "cls"
    os.system(command)
    
def get_value(information_about_input_value, data_format = "str",separator = "-"):
    """get value from user

    Args:
        geting value from user

    Returns:
        string or int, depends what we need from user
    """
    while True:
        try:
            match data_format:
                case "str":
                    try:
                        string_to_search = str(input(information_about_input_value))
                        return string_to_search
                    except ValueError:
                        print("Please enter a string to search")
                case "int":
                    try:
                        string_to_search = int(input(information_about_input_value))
                        return string_to_search
                    except ValueError:
                        print("Please enter a intiger to search")
                case "datetime":
                    try:
                        string_to_search = str(input(information_about_input_value))
                        try:
                            day , month , year = str(string_to_search).split(separator) 
                        except:
                            print(f"Please use {separator} to separate date")

                        date = datetime.datetime(int(year), int(month), int(day))    
                        return date
                    except ValueError:
                        print("Please enter a datetime to search")      
        except:
            print("Please select format from: str, int, datetime")


def name(name_of_file,name_of_file2 = ""):
    """
    ####### name(name_of_file): ##########
    # FUNCTION RETURN WHOLE PATH TO FILE #
    ######################################
    """ 
    file_path = os.path.abspath(os.getcwd())
    if name_of_file2 != "":
        name =  file_path + "\\" + name_of_file + "\\" + name_of_file2
    else:
        name =  file_path + "\\" + name_of_file
    return str(name)
