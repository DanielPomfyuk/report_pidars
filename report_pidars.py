from selenium import webdriver
from webpage_elements import *
import json

print("Slava Ukrayini")
with open("./dolboebi.json", "r") as read_file:
    dolboebi = json.load(read_file)

# set up the web driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com")

# accept_cookies & log in
accept_cookies(driver)
log_in(driver)

# report pidars
posts_counter = 0
for index in dolboebi:
    dolboeb = dolboebi[index]
    print(f"Reporting this dolboeb: {dolboeb['username']}")
    for post in dolboeb["posts"]:
        report_post(driver,post)
        posts_counter+=1
    print(f"Posts reported in total: {posts_counter}")
time.sleep(5)
driver.quit()
