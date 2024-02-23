"""
In normal dropdown sitioation we are using select method
and there we have select TAG in html page
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

country_inbox = driver.find_element(By.XPATH, "//span[@class='select2-selection__rendered' and @id='select2-billing_country-container'] ")
country_inbox.click()

list_of_countries = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']/li")

for country in list_of_countries:
    if country.text == "Germany":
        country.click()
        break
    
Phone_number = driver.find_element(By.XPATH, "//input[@class='input-text thwcfe-input-field' and @id='billing_phone']").send_keys("+91 98855 14939")


time.sleep(3)
driver.quit()