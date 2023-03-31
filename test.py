import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()


driver.get('http://127.0.0.1:8000/accounts/login/')

time.sleep(4)

username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')
username.send_keys('Malay')
password.send_keys('Malay2004')
password.send_keys(Keys.RETURN)
time.sleep(4)
driver.quit()
