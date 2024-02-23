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
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#date feilds clicking
date_of_birth = driver.find_element(By.XPATH, "//input[@id='dob']").click()


web_year = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']")
date_picker_year = Select(web_year)
date_picker_year.select_by_visible_text("1992")

web_month = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div[1]/div/select[1]")
date_picker_month = Select(web_month)
date_picker_month.select_by_visible_text("May")

web_all_days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for day in web_all_days:
       if day.text == "22":
              day.click()
              break
       




time.sleep(5)
driver.quit()