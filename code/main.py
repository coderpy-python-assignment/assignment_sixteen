import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options
chrome_options = Options()
prefs = {"profile.default_content_setting_values.notifications": 1}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.facebook.com/')

# 1. Login
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
)
email_field.send_keys('tutedude5@gmail.com')

password_field = driver.find_element(By.ID, "pass")
password_field.send_keys('test@123')

login_btn = driver.find_element(By.NAME, "login")
login_btn.click()

# 2. Wait for homepage
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Home"]'))
).click()

# 3. Click "What's on your mind"
find_post_ele = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), \"What's on your mind\")]"))
)
find_post_ele.click()

# 4. Wait for post input to appear
status = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
)
status.click()
status.send_keys("Hello Everyone! Nice to see you here.")

# 2. Click the Post button
post_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Post']/ancestor::div[@role='button']"))
)
post_button.click()

# Optional: You can add logic to click "Post" button if needed
time.sleep(10)

# Quitting driver
driver.quit()

