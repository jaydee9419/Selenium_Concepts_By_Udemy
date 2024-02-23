# CSS Selector combinations

# 1. tag and id
# 2. tag and class
# 3. tag and Attribute
# 4. tag, class and attribute


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#calling browser
driver = webdriver.Edge()

#Maximizing the window
driver.maximize_window()

#Opening required side by pssing url
driver.get("https://admin-demo.nopcommerce.com/login")
time.sleep(3)

#fining search element by ID CSS_SELECTOR
# # 1. tag and id (tagname#valueofid)
# email = driver.find_element(By.CSS_SELECTOR, 'input#Email')
# email.clear()
# time.sleep(2)
# email.send_keys("abc")

#                 #or
# email = driver.find_element(By.CSS_SELECTOR, "#Email")
# email.clear()
# time.sleep(2)
# email.send_keys("abc")


# # 2. tag and class (tagname.valueofclass)
# password = driver.find_element(By.CSS_SELECTOR, "input.password")
# password.clear()
# time.sleep(2)
# password.send_keys("123")

                #or
# password = driver.find_element(By.CSS_SELECTOR, ".password")
# password.clear()
# time.sleep(2)
# password.send_keys("123")


# 3. tag and Attribute (tagname[attribute = value])
# mail = driver.find_element(By.CSS_SELECTOR, "input[type=email]")
# mail.clear()
# time.sleep(2)
# mail.send_keys("123")

                #or
# mail = driver.find_element(By.CSS_SELECTOR, "[type=email]")
# mail.clear()
# time.sleep(2)
# mail.send_keys("123")


# 4. tag, class and attribute (tagname.valueofclass[attribute = value])
# mail = driver.find_element(By.CSS_SELECTOR, "input.email[type = email]")
# mail.clear()
# time.sleep(2)
# mail.send_keys("123")

                    #or
mail = driver.find_element(By.CSS_SELECTOR, ".email[type = email]")
mail.clear()
time.sleep(2)
mail.send_keys("123")

time.sleep(3)
driver.quit