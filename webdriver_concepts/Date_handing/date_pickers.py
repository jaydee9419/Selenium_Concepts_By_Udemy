"""
Date Picker / Calendar relevant
---------------------------------
There are two types of web elements
1. Standard (Eg: Buttons, Radio buttons, checkboxes etc.)

2. Non-standard (customized elements)
   - will not be the same on every page

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://jqueryui.com/datepicker/")

#finding xpath of frame
frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

#swithing to frame area
driver.switch_to.frame(frame)


# # Approch 1 - sendkeys() method
# #================================================
# # pass date directly to the input feilds

# #finding xpath of input feild
# date_input = driver.find_element(By.XPATH, "//input[@id='datepicker']")
# # date format: MM/DD/YYYY
# date_input.send_keys("12/10/2023")

# Approch 2 - 
#================================================
# pass date directly to the input feilds

#expected date
exp_year = "1992"
exp_month = "May"
exp_day = "22"

time.sleep(2)
# #finding xpath of input feild
date_input = driver.find_element(By.XPATH, "//input[@id='datepicker']")
# date format: MM/DD/YYYY
date_input.click()
time.sleep(1)

while True:
    web_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    web_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    
    if web_month == exp_month and web_year == exp_year:
        break;
    else:
        # if we wanna future date
        # next_arrow = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
        
        #if we wanna god to back date
        prev_arrow = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()
        
    
#select date
web_all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for web_day in web_all_dates:
    if web_day.text == exp_day:
        web_day.click()
        break
    
# reaching correct date

time.sleep(3)
driver.quit()
