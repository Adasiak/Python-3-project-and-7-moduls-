from lib import *
import requests
from selenium import webdriver
import time
from random import randint

clearConsole()

driver = webdriver.Chrome()
time.sleep(randint(2,6))
# Maximize the window and let code stall 
driver.maximize_window()
time.sleep(randint(4,8))
driver.get("https://sklep.pgg.pl/")
time.sleep(randint(3,7))

while True:
    try:
        button = driver.find_element_by_link_text("Submit")
        time.sleep(randint(1,3))    
        if button is not None:
            button.click()
    except:
        driver.refresh()
    time.sleep(randint(3,6))

