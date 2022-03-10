import sys
import time
from css_selectors import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import bcolors


def findElementBySelector(driver, css_selector, timeout=10, reloaded=False):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    except:
        if not reloaded:
            reload(driver)
            findElementBySelector(driver,css_selector,timeout, True)
        else:
            raise
        


def findElementByXPath(driver, xpath, timeout=10, reloaded=False):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        if not reloaded:
            reload(driver)
            findElementByXPath(driver,xpath,timeout, True)
        else:
            raise

def findElementById(driver, id,timeout=10, reloaded=False):
        return WebDriverWait(driver, timeout).until(EC.presence_of_all_elements_located((By.ID, id)))

def reload(driver):
    reload_button = findElementById(driver,RELOAD_BUTTON,5)
    reload_button.click()

def accept_cookies(driver: webdriver):
    try:
        cookie_button = findElementBySelector(
            driver, ALLOW_COOKIES_BUTTON)
        cookie_button.click()
    except:
        print("Couldn't accept the cookies")
        driver.quit()
        sys.exit()


def insert_credantials(driver: webdriver, username: str, password: str):
    print("logging in using the credentials from")
    username_input = findElementBySelector(driver, USERNAME_INPUT)
    username_input.send_keys(username)
    password_input = findElementBySelector(driver, PASSWORD_INPUT)
    password_input.send_keys(password)
    submit_button = findElementBySelector(
        driver, SUBMIT_CREDENTIALS_BUTTON)
    submit_button.click()


def wait_for_code(driver: webdriver):
    try:
        findElementByXPath(driver, LOCK)
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


def log_in(driver: webdriver, username, password):
    try:
        insert_credantials(driver, username, password)
        wait_for_code(driver)
        notifications_off(driver)
    except:
        print(f"{bcolors.FAIL}Couldn't Log in. Sutting down the browser{bcolors.ENDC}")
        driver.quit()
        sys.exit()


def follow(driver: webdriver, username: str):
    try:
        driver.get(f"{BASE_PATH}{username}")
        follow_button = findElementByXPath(driver, FOLLOW_BUTTON)
        follow_button.click()
        print("Started following this dolboeb: ",
              f"{bcolors.OKGREEN}{username}{bcolors.ENDC}")
    except:
        return


def unfollow(driver: webdriver, username: str):
    try:
        driver.get(f"{BASE_PATH}{username}")
        after_follow = findElementBySelector(driver, AFTER_FOLLOW)
        after_follow.click()
        unfollow_button = findElementByXPath(driver, UNFOLLOW_BUTTON)
        unfollow_button.click()
        findElementByXPath(driver, FOLLOW_BUTTON)
        print("Successfully unfollowed this dolboeb: ",
              f"{bcolors.OKGREEN}{username}{bcolors.ENDC}")
    except:
        print(f"{bcolors.FAIL}Didn't manage to unfollow {username}{bcolors.ENDC}")
        return


def report_user(driver: webdriver, username: str):
    try:
        driver.get(f"{BASE_PATH}{username}")
        more_options = findElementBySelector(driver, MORE_OPTIONS_BUTTON_USER)
        more_options.click()
        report_button = findElementByXPath(driver, REPORT_BUTTON)
        report_button.click()
        report_account_button = findElementByXPath(
            driver, REPORT_ACCOUNT_BUTTON)
        report_account_button.click()
        reason_button = findElementBySelector(driver, REASON_BUTTON)
        time.sleep(3)
        reason_button.click()
        false_information = findElementByXPath(driver, FALSE_INFORMATION)
        false_information.click()
        print(
            "Successfully reported user: " f"{bcolors.OKGREEN}{username}{bcolors.ENDC}")
        return True
    except:
        print(
            f"{bcolors.FAIL}Didn't manage to report the user{bcolors.ENDC}")
        return False


def report_post(driver: webdriver, link):
    try:
        driver.get(link)
        more_options = findElementBySelector(driver, MORE_OPTIONS_BUTTON_POST)
        more_options.click()
        report_button = findElementByXPath(driver, REPORT_BUTTON)
        report_button.click()
        false_information = findElementByXPath(driver, FALSE_INFORMATION)
        false_information.click()
        politics_reason = findElementByXPath(driver, POLITICS_REASON)
        politics_reason.click()
        close_button = findElementBySelector(driver, CLOSE_BUTTON)
        close_button.click()
        print(
            "Successfully reported post " f"{bcolors.OKGREEN}{link}{bcolors.ENDC}")
        return True
    except:
        print(f"{bcolors.FAIL}Couldn't report post {link}{bcolors.ENDC}")
        return False
