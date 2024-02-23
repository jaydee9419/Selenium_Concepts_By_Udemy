"""
Taking screenshot of webpage

- driver.get_screenshot("path needs to provide along with format")

# if we want take screenshot and save in current working directory
- driver.get_screenshot(os.getcwd()+"123.fileformat")
- driver.get_screenshot_os_file(os.getcwd()+"123.fileformat")

# if we want to get screen shot securely like in binary format
- driver.get_screenshot_as_png()needs to convert this binary file in to readable file
- driver.get_screenshot_as_base64() needs to convert this binary file in to readable file
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://demo.nopcommerce.com/")

#capture screen shot
driver.save_screenshot("C:\\Users\\11571\\Downloads\\screenshots\\homepage.png")



time.sleep(5)
driver.quit()