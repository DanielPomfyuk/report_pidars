from selenium import webdriver
from webpage_elements import *
from css_selectors import bcolors
import json

print(f"{bcolors.OKBLUE}Slava {bcolors.ENDC}",
      f"{bcolors.WARNING}Ukrayini{bcolors.ENDC}")
with open("./dolboebi.json", "r") as read_file:
    dolboebi = json.load(read_file)

# set up the web driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com")

# accept_cookies & log in
accept_cookies(driver)
log_in(driver)

# report pidars
posts_counter = 0
for index in dolboebi:
    dolboeb = dolboebi[index]
    print("Reporting this dolboeb: ",
          f"{bcolors.OKGREEN}{dolboeb['username']}{bcolors.ENDC}")
    for post in dolboeb["posts"]:
        try:
            report_post(driver, post)
            posts_counter += 1
        except:
            print(f"{bcolors.FAIL}Couldn't report the post. Moving to the next one{bcolors.ENDC}")
            continue
print(f"{bcolors.OKGREEN}Posts reported in total: {posts_counter}{bcolors.ENDC}")
driver.quit()
