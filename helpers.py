from selenium import webdriver
from webpage_elements import *
from css_selectors import bcolors
import json

def displayChant():
    print(f"{bcolors.OKBLUE}Slava {bcolors.ENDC}",
      f"{bcolors.WARNING}Ukrayini{bcolors.ENDC}")

def init(file_name):
    # set up a dictionary with all the users & posts
    with open(file_name, "r") as read_file:
        dolboebi = json.load(read_file)
    
    # set up the webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return dolboebi,driver
