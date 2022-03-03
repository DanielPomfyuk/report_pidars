from os import system
import time
from css_selectors import *
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import toml

config = toml.load("./config.toml")


def findElementBySelector(driver, timeout, css_selector):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def findElementByXPath(driver,timeout, xpath):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))


def accept_cookies(driver: webdriver):
    logging.info("accepting cookies. yum yum")
    cookie_button = findElementBySelector(driver, 10, ALLOW_COOKIES_BUTTON)
    cookie_button.send_keys(Keys.RETURN)


def insert_credantials(driver: webdriver):
    logging.info("logging in using the credentials from ./config.toml")
    username_input = findElementBySelector(driver, 10, USERNAME_INPUT)
    username_input.send_keys(config.get('credentials').get('username'))
    password_input = findElementBySelector(driver, 10, PASSWORD_INPUT)
    password_input.send_keys(config.get('credentials').get('password'))
    submit_button = findElementBySelector(driver, 10, SUBMIT_CREDENTIALS_BUTTON)
    submit_button.click()


def wait_for_code(driver: webdriver):
    logging.info(
        "Please enter the code ,sent to your phone number.\nWaiting for 2 minutes")
    dont_save_button = findElementBySelector(driver, 120, DONT_SAVE_PASSWORD_BUTTON)
    dont_save_button.click()


def notifications_off(driver: webdriver):
    notifications_off_button = findElementBySelector(
        driver, 10, DONT_TURN_ON_NOTIFICATIONS_BUTTON)
    notifications_off_button.click()


def log_in(driver: webdriver):
    try:
        insert_credantials(driver)
        wait_for_code(driver)
        notifications_off(driver)
    except:
        print("Something went wrong. Sutting down the browser")
        driver.quit()
        system.exit()
    time.sleep(2)

def report_post(driver: webdriver, link):
    try:
        driver.get(link)
        post = findElementBySelector(driver,10,POST)
        post.click()
        more_options = findElementBySelector(driver,1000,MORE_OPTIONS_BUTTON)
        more_options.click()
        report_button = findElementBySelector(driver,1000,REPORT_BUTTON)
        report_button.click()
        false_information = findElementBySelector(driver,1000,FALSE_INFORMATION)
        false_information.click()
        politics_reason = findElementByXPath(driver,1000,POLITICS_REASON)
        politics_reason.click()
        close_button = findElementBySelector(driver,1000,CLOSE_BUTTON)
        close_button.click()
    except:
        print("Something went wrong. Sutting down the browser")
        driver.quit()
        system.exit()
