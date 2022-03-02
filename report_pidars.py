from selenium import webdriver
from webpage_elements import *
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("https://www.instagram.com")
accept_cookies(driver)

time.sleep(5)
driver.quit()