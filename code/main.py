import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
email_field    = driver.find_element(By.XPATH,'.//*[@id="email"]')
email_field.send_keys('vegesaj663@iridales.com')
password_field = driver.find_element(By.XPATH,'.//*[@id="pass"]')
password_field.send_keys('test@123')
login_btn      = driver.find_element(By.XPATH,'//*[@id="loginbutton"]') # everytime this button is changing
login_btn.click()

status         = driver.find_element(By.XPATH,'//*[@name="xhpc_message"]')
time.sleep(5)

status.send_keys('Hello Everyone ! Nice to see here :smile')
time.sleep(10)

