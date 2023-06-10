from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
from faker import Faker
import time
import random
from selenium.common.exceptions import TimeoutException
import requests

load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "BROWSERSTACK_USERNAME"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "BROWSERSTACK_ACCESS_KEY"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "103.0",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Firefox",
        "browserVersion": "102.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Safari",
        "browserVersion": "14.1",
        "os": "OS X",
        "osVersion": "Big Sur",
        "sessionName": "BStack Python sample parallel",
        "buildName": BUILD_NAME,
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)

    fake = Faker()
    wait = WebDriverWait(driver, 10)

    def delay():
        time.sleep(random.randint(1, 3))

    try:
        driver.get('https://qasvus.wordpress.com')

        # API testing
        print("qasvus Url has", requests.get("https://qasvus.wordpress.com").status_code, "as status Code")
        code = requests.get("https://qasvus.wordpress.com").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check browser title
        try:
            assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
            print("Page has", driver.title + " as Page title")
        except AssertionError:
            print("Assertion Error for Title. Current title is: ", driver.title)

        # Check cookie button is clickable ?
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Close and accept']")))
            driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
        except TimeoutException:
            print("Couldn't find a button Close and accept")

        # Check all presentable fields
        driver.find_element(By.XPATH, "//h2[contains(.,'Send Us a Message')]").is_displayed()
        driver.find_element(By.XPATH, "//label[contains(.,'Name(required)')]").is_displayed()
        driver.find_element(By.XPATH, "//label[contains(.,'Email(required)')]").is_displayed()
        driver.find_element(By.XPATH, "//label[contains(.,'Message')]").is_displayed()

        # filling in the form first_name, email, message
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-name')]").send_keys(fake.first_name())
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-email')]").send_keys(fake.email())
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(fake.text())

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Submit')]")))
            driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
        except TimeoutException:
            print("Couldn't find a button Submit")

        # Delay all actions from 1 to 3 sec
        delay()

        # check messages is send ?
        driver.find_element(By.XPATH, "//h4[contains(.,'Your message has been sent')]").is_displayed()

        # Delay all actions from 1 to 3 sec
        delay()

        # Find "go back" button (link) and go back to the Main page.

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))
            driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()
        except TimeoutException:
            print("Couldn't find a Go back Submit")

        delay()
    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
        # Stop the driver
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
