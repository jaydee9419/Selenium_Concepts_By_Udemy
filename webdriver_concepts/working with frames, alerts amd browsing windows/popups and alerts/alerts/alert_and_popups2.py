from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

#opens the alert window
signin = driver.find_element(By.XPATH, '//input[@name="proceed"]')
signin.click()
time.sleep(2)

alert_window = driver.switch_to.alert
time.sleep(2)
print(alert_window.text)
time.sleep(2)
alert_window.accept()

time.sleep(2)
driver.quit()