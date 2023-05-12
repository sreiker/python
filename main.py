from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

username = "prashantsharma@lambdatest.com"
pd = "aARUSH@123"
url = "https://accounts.lambdatest.com/login"

driver = webdriver.Chrome()
driver.get(url)

uname = driver.find_element("id", "email")
uname.send_keys(username)
password = driver.find_element("id", "password")
password.send_keys(pd)
driver.find_element("id", "login-button").click()
time.sleep(10)

