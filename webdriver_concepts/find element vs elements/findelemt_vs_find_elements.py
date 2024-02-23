#findelemt vs find_elements
"""
find_element
-----------------
- returns single web element
- if element not find then return no such element excption 
"""
 
"""
find_elemets
-----------------
- returns multiple web elements in the form of list
- if elemenet is not find then simply returns zero and no exception error 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")


#             #find_element() - returns single web element
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# # 1. Locator matching with the single element
# search_box = driver.find_element(By.ID, 'small-searchterms')
# search_box.send_keys("Nokia")
# time.sleep(2)

#---------------------------------------------------------------------
# # 2. Locator matching with the multiple elements
# # Even we triggered to get all the links at web page it finds only 1st link because of we have used find_element instade of find_elements
# footer_links = driver.find_element(By.XPATH, "//div[@class = 'footer']//a")
# print("Links available at footer section: ",footer_links.text)
# time.sleep(2)

#---------------------------------------------------------------------
# # 3. if the element is not find in we page (returns no such elememt exeption)
# # we have used htm in xpath instaded of html
# login_link = driver.find_element(By.XPATH, '/htm/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
# login_link.click()

#---------------------------------------------------------------------


           #find_elements() - returns single web element
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# # 1. Locator matching with the single element
# search_box = driver.find_elements(By.ID, 'small-searchterms')

# # we are not getting directly send keys method because of we have used multiple find_elements method (This is returned as list item not web element)
# #search_box.sendkeys("Hello")

# # we can get the no of items from selected items
# print("No of items find in this element: ",len(search_box))

# # here we can use sendkeys method after identifing the idex of search box from the selected elements
# search_box[0].send_keys("Hello")
# time.sleep(2)

#---------------------------------------------------------------------
# # 2. Locator matching with the multiple elements
# footer_links = driver.find_elements(By.XPATH, "//div[@class = 'footer']//a")

# #to check nop if itesm selected un this elements menthod
# print("No of items find in this element: ",len(footer_links))

# # print specific item from the list of all items by using index value of the perticular item
# print(footer_links[0].text)

# # if we want to print all the elements 
# for each_item in footer_links:
#     print(each_item.text)
# time.sleep(2)

#---------------------------------------------------------------------
# # 3. if the element is not find in we page (this find_elements will not returns no such elememt exeption)
# # we have used htm in xpath instaded of html
# login_link = driver.find_elements(By.XPATH, '/htm/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')

# # if not identify any of the elememnt just it return only 0 
# print(len(login_link))


time.sleep(2)
driver.quit()


