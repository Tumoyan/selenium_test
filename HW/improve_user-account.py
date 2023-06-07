import random
import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()

driver = webdriver.Chrome()
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

# filling in the form
driver.find_element(By.ID, "input-firstname").send_keys(fake.name())
driver.find_element(By.ID, "input-lastname").send_keys(fake.last_name())

# input random email and phone
driver.find_element(By.ID, "input-email").send_keys(str(random.randint(0, 99999)) + "@example.com")
driver.find_element(By.ID, "input-telephone").send_keys(fake.phone_number())

fakePassword = fake.password()
password = driver.find_element(By.ID, "input-password")
password.send_keys(fakePassword)

password_confirm = driver.find_element(By.ID, "input-confirm")
password_confirm.send_keys(fakePassword)

driver.find_element(By.XPATH, "//label[@for='input-newsletter-yes']").click()

driver.find_element(By.XPATH, "//label[@for='input-agree']").click()

driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# asserting that the browser title is correct
# assert driver.title == "Your Account Has Been Created!"

try:
    assert driver.title == "Your Account Has Been Created!"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
try:
    assert driver.title == "My Account"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "//h2[contains(.,'My Account')]").is_displayed()
driver.find_element(By.XPATH, "//h2[contains(.,'My Orders')]").is_displayed()
driver.find_element(By.XPATH, "//h2[contains(.,'My Affiliate Account')]").is_displayed()
driver.find_element(By.XPATH, "//aside[@id='column-right']").is_displayed()

# find pic with user account
driver.find_element(By.XPATH, '//i[@class="fas fa-2x mb-1 fa-user-edit"]').is_displayed()

driver.find_element(By.LINK_TEXT, "Edit Account").click()
time.sleep(0.5)

try:
    assert driver.title == "My Account Information"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.LINK_TEXT, "Password").click()
time.sleep(0.5)

try:
    assert driver.title == "Change Password"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

fakePassword = fake.password()
password = driver.find_element(By.ID, "input-password")
password.send_keys(fakePassword)

password_confirm = driver.find_element(By.ID, "input-confirm")
password_confirm.send_keys(fakePassword)

driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(1)
driver.find_element(By.XPATH,
                    "(//div[contains(.,'Success: Your password has been successfully updated.')])[4]").is_displayed()

try:
    assert driver.title == "My Account"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.LINK_TEXT, "Address Book").click()
time.sleep(0.5)

try:
    assert driver.title == "Address Book"
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "//a[contains(text(),'New Address')]").click()
time.sleep(0.5)

# filling in the address form
first_name = driver.find_element(By.ID, "input-firstname")
first_name.send_keys(fake.first_name())
last_name = driver.find_element(By.ID, "input-lastname")
last_name.send_keys(fake.last_name())
driver.find_element(By.ID, "input-address-1").send_keys(fake.address())
driver.find_element(By.ID, "input-city").send_keys(fake.city())
driver.find_element(By.ID, "input-postcode").send_keys(fake.postcode())
driver.find_element(By.XPATH, "//select[@name='country_id']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="input-country"]/option[240]').click()
time.sleep(0.5)
driver.find_element(By.ID, "input-zone").click()
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="input-zone"]/option[2]').click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

time.sleep(1)
driver.find_element(By.XPATH,
                    "(//div[contains(.,'Your address has been successfully added')])[4]").is_displayed()

# closing the browser
driver.quit()
