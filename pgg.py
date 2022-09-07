from lib import *
import requests
from selenium import webdriver
import time

clearConsole()


# import module
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.

path_to_file = name("chromedriver")

print(path_to_file)


driver = webdriver.Chrome(path_to_file)
  
# # get https://www.geeksforgeeks.org/
# driver.get("https://www.geeksforgeeks.org/")
  
# # Maximize the window and let code stall 
# # for 10s to properly maximise the window.
# driver.maximize_window()
# time.sleep(10)
  
# # Obtain button by link text and click.
# button = driver.find_element_by_link_text("Sign In")
# button.click()