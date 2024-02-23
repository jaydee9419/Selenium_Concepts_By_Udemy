from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://books-pwakit.appspot.com/")

# Locate the shadow host
shadow_host = driver.find_element(By.CSS_SELECTOR, 'body > book-app')

# Access the Shadow DOM
search_box = driver.execute_script('return arguments[0].shadowRoot.querySelector(".menu-btn")', shadow_host)

search_box.click()

time.sleep(5)

about = driver.execute_script('return arguments[0].shadowRoot.evaluate("")', shadow_host)

time.sleep(10)

driver.quit()



