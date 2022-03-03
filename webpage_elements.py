import sys
import toml
import logging
from css_selectors import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
config = toml.load("./config.toml")


def findElementBySelector(driver, timeout, css_selector):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))


def findElementByXPath(driver, timeout, xpath):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))


def accept_cookies(driver: webdriver):
    logging.info("accepting cookies. yum yum")
    try:
        cookie_button = findElementBySelector(
            driver, 1000, ALLOW_COOKIES_BUTTON)
        cookie_button.click()
    except:
        print("Could not accept the cookies")
        driver.quit()
        sys.exit()


def insert_credantials(driver: webdriver):
    logging.info("logging in using the credentials from ./config.toml")
    username_input = findElementBySelector(driver, 10, USERNAME_INPUT)
    username_input.send_keys(config.get('credentials').get('username'))
    password_input = findElementBySelector(driver, 10, PASSWORD_INPUT)
    password_input.send_keys(config.get('credentials').get('password'))
    submit_button = findElementBySelector(
        driver, 10, SUBMIT_CREDENTIALS_BUTTON)
    submit_button.click()


def wait_for_code(driver: webdriver):
    try:
        lock = findElementByXPath(driver, 10, LOCK)
        logging.info(
            "Please enter the code ,sent to your phone number.\nWaiting for 2 minutes")
        dont_save_button = findElementBySelector(
            driver, 120, DONT_SAVE_PASSWORD_BUTTON)
        dont_save_button.click()
    except:
        return


def notifications_off(driver: webdriver):
    notifications_off_button = findElementByXPath(
        driver, 1000, DONT_TURN_ON_NOTIFICATIONS_BUTTON)
    notifications_off_button.click()


def log_in(driver: webdriver):
    try:
        insert_credantials(driver)
        wait_for_code(driver)
        notifications_off(driver)
    except:
        print("Couldn't Log in. Sutting down the browser")
        driver.quit()
        sys.exit()


def report_post(driver: webdriver, link):
    driver.get(link)
    more_options = findElementBySelector(driver, 10, MORE_OPTIONS_BUTTON)
    more_options.click()
    report_button = findElementByXPath(driver, 10, REPORT_BUTTON)
    report_button.click()
    false_information = findElementByXPath(driver, 10, FALSE_INFORMATION)
    false_information.click()
    politics_reason = findElementByXPath(driver, 10, POLITICS_REASON)
    politics_reason.click()
    close_button = findElementBySelector(driver, 10, CLOSE_BUTTON)
    close_button.click()
