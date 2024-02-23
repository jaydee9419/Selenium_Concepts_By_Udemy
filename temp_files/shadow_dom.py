# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time




# driver = webdriver.Chrome()

# driver.get("https://books-pwakit.appspot.com/")

# # treditional method
# # search_box = driver.find_element(By.XPATH, "//*[@id='input']")

# # Shadow new method
# search_box = driver.execute_script('return document.querySelector("body > book-app").shadowRoot.querySelector("#input")')

# # for clicking
# # driver.execute_script('arguments[0].click();', search_box)

# # for input text send 
# driver.execute_script('arguments[0].setAttribute("value","Hello");', search_box)

# # search_box.send_keys("Hello")


# time.sleep(10)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://books-pwakit.appspot.com/")

# Locate the shadow host
shadow_host = driver.find_element(By.CSS_SELECTOR, 'body > book-app')

# Access the Shadow DOM
search_box = driver.execute_script('return arguments[0].shadowRoot.querySelector("#input")', shadow_host)

# Input text using send_keys
search_box.send_keys("Hello")

# clicking enter
search_box.send_keys(Keys.ENTER)

time.sleep(10)

driver.quit()
