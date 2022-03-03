import sys
import toml
import logging
from css_selectors import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
config = toml.load("./config.toml")


def findElementBySelector(driver, css_selector, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def findElementByXPath(driver, xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))


def accept_cookies(driver: webdriver):
    print("accepting cookies. yum yum")
    try:
        cookie_button = findElementBySelector(
            driver, ALLOW_COOKIES_BUTTON)
        cookie_button.click()
    except:
        print("Could not accept the cookies")
        driver.quit()
        sys.exit()


def insert_credantials(driver: webdriver):
    print("logging in using the credentials from ./config.toml")
    username_input = findElementBySelector(driver, USERNAME_INPUT)
    username_input.send_keys(config.get('credentials').get('username'))
    password_input = findElementBySelector(driver, PASSWORD_INPUT)
    password_input.send_keys(config.get('credentials').get('password'))
    submit_button = findElementBySelector(
        driver,SUBMIT_CREDENTIALS_BUTTON)
    submit_button.click()


def wait_for_code(driver: webdriver):
    try:
        lock = findElementByXPath(driver, LOCK)
        print(
            "Please enter the code ,sent to your phone number.\nWaiting for 2 minutes")
        dont_save_button = findElementBySelector(
            driver, DONT_SAVE_PASSWORD_BUTTON, 120)
        dont_save_button.click()
    except:
        return


def notifications_off(driver: webdriver):
    notifications_off_button = findElementByXPath(
        driver, DONT_TURN_ON_NOTIFICATIONS_BUTTON)
    notifications_off_button.click()


def log_in(driver: webdriver):
    try:
        insert_credantials(driver)
        wait_for_code(driver)
        notifications_off(driver)
    except:
        logging.ERROR("Couldn't Log in. Sutting down the browser")
        driver.quit()
        sys.exit()


def report_post(driver: webdriver, link):
    try:
        driver.get(link)
    except:
        return
    more_options = findElementBySelector(driver, MORE_OPTIONS_BUTTON)
    more_options.click()
    report_button = findElementByXPath(driver, REPORT_BUTTON)
    report_button.click()
    false_information = findElementByXPath(driver, FALSE_INFORMATION)
    false_information.click()
    politics_reason = findElementByXPath(driver, POLITICS_REASON)
    politics_reason.click()
    close_button = findElementBySelector(driver, CLOSE_BUTTON)
    close_button.click()
