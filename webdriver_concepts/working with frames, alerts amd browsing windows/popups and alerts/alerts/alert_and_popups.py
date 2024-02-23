"""
alerts or popups
----------------------
- alert window is not a web element we can not perform any action directly
- .switch_to.alert will use to capture alert window

methods using
-------------
alert_window = driver.switch_to.alert

alert_window.text
alert_window.accept()
alert_window.dismiss()
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

#opens the alert window
button = driver.find_element(By.XPATH, '//input[@id="promptexample"]')
button.click()
time.sleep(2)

#access alert window
alert_window = driver.switch_to.alert

# capture text from alert window
print(alert_window.text)

# want to pass some input to the alert window box
alert_window.send_keys("Welcome")
time.sleep(2)

# want to close alert window by clicking ok or cancel button
# # to click Ok button
alert_window.accept()

# to click cancel button
# alert_window.dismiss()

time.sleep(5)
driver.quit()