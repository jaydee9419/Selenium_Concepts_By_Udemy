from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#calling browser
driver = webdriver.Edge()

#Maximizing the window
driver.maximize_window()

#Opening required side by pssing url
driver.get("http://demo.nopcommerce.com/")

# #fining search element by ID 
# search_bar = driver.find_element(By.ID, "small-searchterms")

#fining search element by NAME 
search_bar = driver.find_element(By.NAME, "q")

#using click Function
search_bar.click()

#passing some test in to the search bar
search_bar.send_keys("Nokia Lumia 1020")

#finding element for search button
search_button = driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button')
search_button.click()


time.sleep(5)

##closing browser
driver.close()