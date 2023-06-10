from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import Helpers as Hp


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
        driver.get(Hp.url_qasvus)
        driver.delete_all_cookies()

        # API testing
        Hp.check_API_Status_Code('https://qasvus.wordpress.com')

        # driver sleep from 1 to 3 seconds
        Hp.delay()

        wait = WebDriverWait(driver, 10)

        # Check browser title
        Hp.assert_title(driver, 'California Real Estate – QA at Silicon Valley Real Estate')

        # Check cookie button is clickable ?
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Close and accept']")))
            driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
        except TimeoutException:
            print("Couldn't find a button Close and accept")

        # Check all presentable fields
        Hp.check_all_presentable_fields(driver)

        # filling in the form first_name, email, message
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-name')]").send_keys(Hp.fake.first_name())
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-email')]").send_keys(Hp.fake.email())
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']") \
            .send_keys(Hp.fake.text())

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Submit')]")))
            driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
        except TimeoutException:
            print("Couldn't find a button Submit")

        # Delay all actions from 1 to 3 sec
        Hp.delay()

        # check messages is send ?
        driver.find_element(By.XPATH, Hp.messageHasBeenSent).is_displayed()

        # Delay all actions from 1 to 3 sec
        Hp.delay()

        # Find "go back" button (link) and go back to the Main page.
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))
            driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()
        except TimeoutException:
            print("Couldn't find a Go back Submit")

        Hp.delay()

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
        driver.get(Hp.url_qasvus)
        driver.delete_all_cookies()

        # API testing
        Hp.check_API_Status_Code('https://qasvus.wordpress.com')

        # driver sleep from 1 to 3 seconds
        Hp.delay()

        wait = WebDriverWait(driver, 10)

        # Check browser title
        Hp.assert_title(driver, 'California Real Estate – QA at Silicon Valley Real Estate')

        # Check cookie button is clickable ?
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Close and accept']")))
            driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
        except TimeoutException:
            print("Couldn't find a button Close and accept")

        # Check all presentable fields
        Hp.check_all_presentable_fields(driver)

        # filling in the form first_name, email, message
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-name')]").send_keys(Hp.fake.first_name())
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-email')]").send_keys(Hp.fake.email())
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']") \
            .send_keys(Hp.fake.text())

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Submit')]")))
            driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
        except TimeoutException:
            print("Couldn't find a button Submit")

        # Delay all actions from 1 to 3 sec
        Hp.delay()

        # check messages is send ?
        driver.find_element(By.XPATH, Hp.messageHasBeenSent).is_displayed()

        # Delay all actions from 1 to 3 sec
        Hp.delay()

        # Find "go back" button (link) and go back to the Main page.
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))
            driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()
        except TimeoutException:
            print("Couldn't find a Go back Submit")

        Hp.delay()

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
        driver.get(Hp.url_qasvus)
        driver.delete_all_cookies()

        # API testing
        Hp.check_API_Status_Code('https://qasvus.wordpress.com')

        # driver sleep from 1 to 3 seconds
        Hp.delay()

        wait = WebDriverWait(driver, 10)

        # Check browser title
        Hp.assert_title(driver, 'California Real Estate – QA at Silicon Valley Real Estate')

        # Check cookie button is clickable ?
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Close and accept']")))
            driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()
        except TimeoutException:
            print("Couldn't find a button Close and accept")

        # Check all presentable fields
        Hp.check_all_presentable_fields(driver)

        # filling in the form first_name, email, message
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-name')]").send_keys(Hp.fake.first_name())
        driver.find_element(By.XPATH, "//input[contains(@id,'g2-email')]").send_keys(Hp.fake.email())
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']") \
            .send_keys(Hp.fake.text())

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Submit')]")))
            driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()
        except TimeoutException:
            print("Couldn't find a button Submit")

        # Delay all actions from 1 to 3 sec
        Hp.delay()

        # check messages is send ?
        driver.find_element(By.XPATH, Hp.messageHasBeenSent).is_displayed()

        # Delay all actions from 1 to 3 sec
        Hp.delay()

        # Find "go back" button (link) and go back to the Main page.
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go back')]")))
            driver.find_element(By.XPATH, "//a[contains(text(),'Go back')]").click()
        except TimeoutException:
            print("Couldn't find a Go back Submit")

        Hp.delay()

    def tearDown(self):
        self.driver.quit()
