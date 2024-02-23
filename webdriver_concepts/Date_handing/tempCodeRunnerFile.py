"""
Date Picker / Calendar relevant
---------------------------------
There are two types of web elements
1. Standard (Eg: Buttons, Radio buttons, checkboxes etc.)

2. Non-standard (customized elements)
   - will not be the same on every page

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://jqueryui.com/datepicker/")

#finding xpath of frame
frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

#swithing to frame area
driver.switch_to.frame(frame)