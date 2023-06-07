from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()

# find "Google Search" field and type "abc" there

driver.find_element(By.NAME, "q").send_keys("abc")
time.sleep(1)
# click on "Google Search" button
driver.find_element(By.NAME, "btnK").click()

# Find and click on the ABC link
driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page").click()
assert "ABC Home Page - ABC.com" in driver.title
print("ABC Page Title is: ", driver.title)

# Find and click on the browser
driver.find_element(By.XPATH, "(//span[contains(.,'browse')])[1]").click()
assert "ABC TV Shows, Specials & Movies" in driver.title
print("ABC TV Shows Title is: ", driver.title)

# assert that tab list (popular, ABC, Freeform, FX etc. is displayed)
driver.find_element(By.XPATH, "//ul[@role='tablist']").is_displayed()

# assert that Steve Harvey card displayed and Click on image
imgSteveHarvey = driver.find_element(By.XPATH, "//img[contains(@alt,'Judge Steve Harvey')]")
imgSteveHarvey.is_displayed()
imgSteveHarvey.click()

time.sleep(1)
assert "Watch Judge Steve Harvey TV Show - ABC.com" in driver.title
print("Watch Judge Steve Harvey TV Show Title is: ", driver.title)

# Create variable for Jimmy webpage URL
SteveHarveyTVShowURL = "https://abc.com/shows/judge-steve-harvey"

# Check if URL for Jimmy webpage URL is the same in the browser during a Test
assert SteveHarveyTVShowURL == driver.current_url
if SteveHarveyTVShowURL != driver.current_url:
    print("Current Steve Harvey Show URL is different and it is: ", driver.current_url)
else:
    print("Current Steve Harvey Show URL is OK: ", driver.current_url)

# assert carousel for seasons video is displayed
driver.find_element(By.XPATH,
                    "//div[@class='tilegroup tilegroup--shows tilegroup--carousel tilegroup--landscape']") \
    .is_displayed()

# Scroll down
driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)

# assert carousel for latest clips is displayed
driver.find_element(By.XPATH,
                    "//div[contains(@class,'tilegroup tilegroup--carousel tilegroup--landscape')]") \
    .is_displayed()

element = driver.find_element(By.XPATH, "//img[@title='Steve Harvey']")
time.sleep(1)

# Scroll down to Steve Harvey img
driver.execute_script("arguments[0].scrollIntoView();", element)

time.sleep(1)

element.click()
time.sleep(1)
assert "Steve Harvey | Judge Steve Harvey" in driver.title
print("Steve Harvey | Judge Steve Harvey Title is: ", driver.title)

# assert full page is displayed
driver.find_element(By.XPATH, "//div[@class='fullWidth__column']").is_displayed()

# closing the browser
driver.quit()
