"""
to swith window
.switch_to.window("need to pass window ID)

to open new tab and window
.switch_to.new_window('tab')
.switch_to.New_window('window')


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://demo.nopcommerce.com/")

# #if we use the below one the registration form will open on the same page
# register = driver.find_element(By.XPATH, "//a[@class='ico-register']").click()

# #selenium 3
# #---------------------------------------------
# # if we want to open in new tab and keep the old page as it is
# registration_link = Keys.CONTROL+Keys.RETURN
# register = driver.find_element(By.XPATH, "//a[@class='ico-register']").send_keys(registration_link)


#selenium 4
#---------------------------------------------
# if we want to open in new tab and keep the old page as it is and switch to the new tab

registration_link = Keys.CONTROL+Keys.RETURN
register = driver.find_element(By.XPATH, "//a[@class='ico-register']")
register.send_keys(registration_link)




time.sleep(15)
driver.quit()