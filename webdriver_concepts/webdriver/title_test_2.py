from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# path = Service(r'D:\Work_Environment\Python\Udemy\Selenium_Python\msedgedriver.exe')
driver = webdriver.Edge()
# driver = webdriver.Edge(service=path)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

# Perform actions on the website
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
email_field.clear()
time.sleep(2)
email_field.send_keys('admin@yourstore.com')

password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
password_field.clear()
time.sleep(2)
password_field.send_keys('admin')

login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button')))
login_button.click()

# Wait for the title to change (if needed)
WebDriverWait(driver, 10).until(EC.title_contains("nopCommerce administration"))

# Capture the title of the page
web_title = driver.title

print(web_title)
exp_title = "Dashboard / nopCommerce administration"

if web_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")

time.sleep(2)
# Close the entire browser, including all windows/tabs
driver.quit()
