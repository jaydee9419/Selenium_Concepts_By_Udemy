from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 


import time 


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

# Send Keys
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Jay Dee")
time.sleep(2)

# Alert window actions
driver.find_element(By.XPATH, "//button[@onclick='myFunctionAlert()']").click()
time.sleep(2)

driver.switch_to.alert.dismiss()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@onclick='myFunctionConfirm()']").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@onclick='myFunctionPrompt()']").click()
time.sleep(2)

alert = driver.switch_to.alert
time.sleep(2)

print(alert.text)
alert.send_keys("Jay Dee")
time.sleep(2)

alert.accept()
time.sleep(2)


# Double click
copy = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")
action = ActionChains(driver)
action.double_click(copy).perform()

#Keyboard Actions


time.sleep(5)


i = 6
while i == 6:
    print("Hello")






