from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#calling browser
driver = webdriver.Edge()

#Maximizing the window
driver.maximize_window()

#Opening required side by pssing url
driver.get("http://demo.nopcommerce.com/")

#fining search element by ID TAG_NAME
links = driver.find_elements(By.TAG_NAME, "a")
links_count = len(links)
print(f"No of links in this page: {links_count}")

time.sleep(3)
driver.close()