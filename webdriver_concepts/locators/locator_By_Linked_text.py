from atexit import register
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#calling browser
driver = webdriver.Edge()

#Maximizing the window
driver.maximize_window()

#Opening required side by pssing url
driver.get("http://demo.nopcommerce.com/")

# #fining search element by LINK_TEXT 
# register_link = driver.find_element(By.LINK_TEXT, "Register")
# register_link.click()

#fining search element by PARTIAL_LINK_TEXT 
register_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Reg")
register_link.click()


time.sleep(5)

##closing browser
driver.close()