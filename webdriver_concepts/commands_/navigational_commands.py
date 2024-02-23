""" 
Navigational commands (These are methods)
----------------------
refresh()
forward()
back()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# calling chrome browser
driver = webdriver.Chrome()

# Maximize window
driver.maximize_window()

#open google page 1st web page
driver.get("https://www.google.com/")
time.sleep(2)

# in the same tab open another or 2nd  web page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)

# Go back to google page 1st web pag
driver.back()
time.sleep(2)

# Again go 2nd web page
driver.forward()
time.sleep(2)

# Refresh the current opened web page
driver.refresh()
time.sleep(2)

driver.quit()