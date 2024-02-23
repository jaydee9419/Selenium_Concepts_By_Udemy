"""
Authentication popups
----------------------
To follow the bellow steps for inject/bypass the authontication fields
------------------------------------------
original url: https://the-internet.herokuapp.com/digest_auth

syntax url : http://username:password@abcd.com
syntax for the below test case : https://admin:admin@the-internet.herokuapp.com/digest_auth
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

# # we will get en authontication popup
# driver.get("https://the-internet.herokuapp.com/digest_auth")

# we need to pass username and password to buypass the alert/popup
driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")


#opens the alert window
# button = driver.find_element(By.XPATH, '//input[@id="promptexample"]')
# button.click()
time.sleep(3)