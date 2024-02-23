"""
eg: <input id='123' name='abc'> Email: </input>
in the above line Email is inner text
in the above axample any attribute can access by using .get_attribute('any_attribute') like name, id or Email.
- .text will return only inner text of the elment (most of the time Links having inner text)
- .get_attribute(('any_attribute'))  will use to get the value of any attribute in the element

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")


email = driver.find_element(By.ID, "Email")
time.sleep(1)
email.clear()
time.sleep(1)
email.send_keys("abc@gamil.com")
time.sleep(1)
# .text will not eturn anything 
print("Result of text: ",email.text)

#.get_attribute("value") will return the value
print("Result of get_attribute: ",email.get_attribute('value'))

login_button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
time.sleep(1)
# .text will not eturn anything 
print("Login_button text is: ",login_button.text)

#.get_attribute("value") will return the value
print("login_button attribute is: ",login_button.get_attribute('type'))



time.sleep(3)
driver.quit()