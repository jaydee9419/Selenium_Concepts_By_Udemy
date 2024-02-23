"""
Download file
====================



"""
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


# below 3 lines required to download files in desired location 
# def Chrome_setup():
#     # below 3 lines required to download files in desired location 
#     preferences = {"download.default_directory": "C:\\Users\\11571\\Downloads\\Docs"}
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("prefs", preferences)
    
#     driver = webdriver.Chrome(options=options)
    
#     return driver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://omayo.blogspot.com/')

upload_button = driver.find_element(By.XPATH, "//input[@id='uploadfile']")

upload_button.send_keys("C:\\Users\\11571\\Downloads\\Docs\\file-sample_100kB.doc")

time.sleep(10)
driver.quit()