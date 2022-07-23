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
    
def get_value(information_about_input_value):
    """get value from user

    Args:
        geting value from user

    Returns:
        string or int, depends what we need from user
    """
    while True:
        try:
            string_to_search = str(input(information_about_input_value))
            return string_to_search
        except ValueError:
            print("Please enter a string to search")
   
