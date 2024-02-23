"""
dropdown
-----------------------------
1st step is to import select from selenium 
2nd identify the area of index in webpage
3rd convert identified are to select method to select the requied option

Select method having the following approches
1. by_visable_text
2. by_index
3. by_value
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://omayo.blogspot.com')

#to find the dropdown area
doc = driver.find_element(By.XPATH, "//select[@id='drop1']")

# open the dropdown by using Select method
drop_doc = Select(doc)

#select the required dropdown option
#approch - 1 (by_visable_text)
# drop_doc.select_by_visible_text('doc 1')

# #approch - 2 (by_index)
# drop_doc.select_by_index(2)

# #approch - 3 (by_value)
# drop_doc.select_by_value("jkl")

#user want to to know total count options
all_options = drop_doc.options
print("Total no of dropdown options available: ",len(all_options))

# if user need to know the options values
for option in all_options:
    print(option.text)
    
#----------------------------------------
# How to select options with out using built in function (like above 3 approches)  
for option in all_options:
    if option.text == 'doc 2':
        option.click()
        break

time.sleep(2)
driver.quit()
