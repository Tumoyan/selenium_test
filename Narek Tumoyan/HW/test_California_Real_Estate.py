from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

fake = Faker()

# Go to qasvus.wordpress.com
driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
print("California Real Estate – QA at Silicon Valley Real Estate", driver.title)

driver.find_element(By.XPATH, "//input[@value='Close and accept']").click()

driver.find_element(By.XPATH, "//h2[contains(.,'Send Us a Message')]").is_displayed()
driver.find_element(By.XPATH, "//label[contains(.,'Name(required)')]").is_displayed()
driver.find_element(By.XPATH, "//label[contains(.,'Email(required)')]").is_displayed()
driver.find_element(By.XPATH, "//label[contains(.,'Message')]").is_displayed()

submit = driver.find_element(By.XPATH, "//button[contains(.,'Submit')]")
submit.is_displayed()

# filling in the form
# first_name
driver.find_element(By.XPATH, "//input[contains(@id,'g2-name')]").send_keys(fake.first_name())
# filling in the form
# email
driver.find_element(By.XPATH, "//input[contains(@id,'g2-email')]").send_keys(fake.email())
# filling in the form
# message
driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(fake.text())

submit.click()

# wait 2 sec, then proceed with script
time.sleep(2)

# check messages is send ?
driver.find_element(By.XPATH, "//h4[contains(.,'Your message has been sent')]").is_displayed()

# wait 2 sec, then proceed with script
time.sleep(2)

# Find "go back" button (link) and go back to the Main page.
driver.back()

# wait 2 sec, then proceed with script
time.sleep(2)

# Once you'll get the Main page, verify it by finding and print "type" for "Submit" button
print(type(submit))

# quit from browser
driver.quit()
