from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

# # 1. select specific checkbox from the list
# # ---------------------------------
# accessories = driver.find_element(By.XPATH, "//*[@id='HTML33']/div[1]/input[1]")
# time.sleep(1)
# accessories.click()
# print(accessories.is_selected())


# 1. select multiple checkboxs from the list
# ---------------------------------
#use find_elements not find_element to check all the checkboxes 
accessories = driver.find_elements(By.XPATH, "//input[@name='accessories']")
print(len(accessories))

#to clear alredy selected items
for item in accessories:
    if item.is_selected():
        item.click()
time.sleep(3)

# ---------------------------------
#if we want to click all the checkboxeses
# for item in range(len(accessories)):
#     accessories[item].click()
#     print(item.get_attribute("value"))  
#     print(item.is_selected())

# ---------------------------------
# for item in accessories:
#     item.click()
#     print(item.get_attribute("value"))  
#     print(item.is_selected())

# ---------------------------------
# #If user want to select only required checkboxes
# for item in accessories:
#     things = item.get_attribute("value")
#     if things == "Laptop" or "Bag" or "Pen":
#         item.click()


# ---------------------------------       
# # if user want to select only last 2 boxex
# for item in range(len(accessories)-2,len(accessories)):
#     accessories[item].click()
        
# if i want to select first 2 boxes
for item in range(len(accessories)):
    if item < 2:
        accessories[item].click()
time.sleep(3)  
     
# if user want to clear all the check boxes
for item in accessories:
    if  item.is_selected():
        item.click()
    


time.sleep(5)
driver.quit()




