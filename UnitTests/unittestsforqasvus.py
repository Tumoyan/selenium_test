import time
from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from faker import Faker


class ChromeTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=en-US')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # self.driver.set_window_size(1820, 1050)
        self.driver.maximize_window()

    def test_Fill_out_all_fields_and_click_on_Submit_button(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.delete_all_cookies()

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        fake = Faker()
        wait = WebDriverWait(driver, 10)

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

    def tearDown(self):
        self.driver.quit()


class EdgeTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.EdgeOptions()
        options.add_argument('--lang=en-US')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()), options=options)
        # self.driver.set_window_size(1820, 1050)
        self.driver.maximize_window()


    def test_Fill_out_all_fields_and_click_on_Submit_button(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.delete_all_cookies()

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        fake = Faker()
        wait = WebDriverWait(driver, 10)

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

    def tearDown(self):
        self.driver.quit()


class FirefoxTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", "en-US")
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
        # self.driver.set_window_size(1820, 1050)
        self.driver.maximize_window()

    def test_Fill_out_all_fields_and_click_on_Submit_button(self):
        driver = self.driver
        driver.get('https://qasvus.wordpress.com')
        driver.delete_all_cookies()

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        fake = Faker()
        wait = WebDriverWait(driver, 10)

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

    def tearDown(self):
        self.driver.quit()