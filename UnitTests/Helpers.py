import time
import random
import requests
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url_qasvus = 'https://qasvus.wordpress.com'
fake = Faker()

# Most often used xPaths
messageHasBeenSent = "//h4[contains(.,'Your message has been sent')]"


def delay():
    time.sleep(random.randint(1, 3))


def check_API_Status_Code(url):
    code = requests.get(url).status_code
    if code == 200:
        print("API response code is OK", requests.get(url).status_code)
    else:
        print("Url has", requests.get(url).status_code, "as status Code")


def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print('Page has', driver.title + 'as Page title')
    driver.get_screenshot_as_file(f'Page {title}.png')
    if not title in driver.title:
        raise Exception(f'Page {title} has wrong Title!')


def check_all_presentable_fields(driver):
    driver.find_element(By.XPATH, "//h2[contains(.,'Send Us a Message')]").is_displayed()
    driver.find_element(By.XPATH, "//label[contains(.,'Name(required)')]").is_displayed()
    driver.find_element(By.XPATH, "//label[contains(.,'Email(required)')]").is_displayed()
    driver.find_element(By.XPATH, "//label[contains(.,'Message')]").is_displayed()
