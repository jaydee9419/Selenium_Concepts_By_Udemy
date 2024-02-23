# class name and tag name used when to find more then one elemet
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#calling browser
driver = webdriver.Edge()

#Maximizing the window
driver.maximize_window()

#Opening required side by pssing url
driver.get("http://automationpractice.com/index.php")

#fining search element by Class_NAME
slides = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(slides))


time.sleep(3)
driver.close()