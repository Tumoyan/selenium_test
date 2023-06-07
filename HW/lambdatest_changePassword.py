import time
from selenium import webdriver
from faker import Faker
from selenium.webdriver.common.by import By

fake = Faker()

driver = webdriver.Chrome()
action = webdriver.ActionChains(driver)
driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

# filling in the form
driver.find_element(By.ID, "input-firstname").send_keys(fake.name())
driver.find_element(By.ID, "input-lastname").send_keys(fake.last_name())

# input random email and phone
fakeEmail = fake.email()
driver.find_element(By.ID, "input-email").send_keys(fakeEmail)
driver.find_element(By.ID, "input-telephone").send_keys(fake.phone_number())

# input hardcode password
driver.find_element(By.ID, "input-password").send_keys("fakePassword")
driver.find_element(By.ID, "input-confirm").send_keys("fakePassword")

driver.find_element(By.XPATH, "//label[@for='input-agree']").click()
driver.find_element(By.XPATH, "//input[@value='Continue']").click()
time.sleep(0.5)

try:
    assert driver.title == "Your Account Has Been Created!"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "//a[contains(.,'Password')]").click()
time.sleep(0.5)

try:
    assert driver.title == "Change Password"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

# input hardcode password
driver.find_element(By.ID, "input-password").send_keys("fakePassword123")
driver.find_element(By.ID, "input-confirm").send_keys("fakePassword123")

driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
time.sleep(0.5)

driver.find_element(By.XPATH,
                    "(//div[contains(.,'Success: Your password has been successfully updated.')])[4]").is_displayed()

driver.find_element(By.XPATH, "(//a[contains(.,'Logout')])[2]").click()
time.sleep(0.5)

try:
    assert driver.title == "Account Logout"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

driver.find_element(By.XPATH, "(//a[contains(.,'Login')])[2]").click()
time.sleep(0.5)

driver.find_element(By.ID, "input-email").send_keys(fakeEmail)
# input changed password
driver.find_element(By.ID, "input-password").send_keys("fakePassword123")
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(0.5)

try:
    assert driver.title == "My Account"
    print("Title is Correct. Current Title is:", driver.title)
except AssertionError:
    print("Title is different. Current Title is:", driver.title)

# closing the browser
driver.quit()
