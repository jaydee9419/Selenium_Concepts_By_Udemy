"""
Keyboard operations
====================



"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('https://text-compare-online.com/')
"""
Performing the below actions
================================
Ctrl+A
Ctrl+C
Tab
Ctrl+V
"""

# finding location of 1st box (left box)
left_box = driver.find_element(By.XPATH, "//textarea[@name='text1']")

# finding location of 2nd box (right box)
right_box = driver.find_element(By.XPATH, "//textarea[@name='text2']")

# sending text to 1st box
left_box.send_keys("Hello World")


# creating actionchains

action = ActionChains(driver)
time.sleep(1)
#Select
#---------
# pressing CTRL button
action.key_down(Keys.CONTROL)
# Passing 'a' means pressing "a" along with Ctrl
action.send_keys('a')
# Release the key from press
action.key_up(Keys.CONTROL)
#perform the activity
action.perform()
# # Or we can write like below
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# time.sleep(1)

#Copy
#---------
# # pressing CTRL button
action.key_down(Keys.CONTROL)
# Passing 'c' means pressing "c" along with Ctrl
action.send_keys('c')
# Release the key from press
action.key_up(Keys.CONTROL)
#perform the activity
action.perform()
# Or we can write like below
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# time.sleep(1)

#Tab button action
#---------
# pressing Tab button 
action.send_keys(Keys.TAB)
# Perform action
action.perform()
# Or we can write like below
# action.send_keys(Keys.TAB).perform()
# time.sleep(1)

#Paste copied data from 1st box to 2nd box
#---------
# pressing CTRL button
action.key_down(Keys.CONTROL)
# Passing 'v' means pressing "v" along with Ctrl
action.send_keys('v')
# Release the key from press
action.key_up(Keys.CONTROL)
#perform the activity
action.perform()
# Or we can write like below
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()



time.sleep(3)
driver.quit()