from css_selectors import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def accept_cookies(driver):
    search = driver.find_element_by_css_selector(ALLOW_COOKIES_BUTTON)
    search.send_keys(Keys.RETURN)
