from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://books-pwakit.appspot.com/")

# Locate the shadow host
shadow_host = driver.find_element(By.CSS_SELECTOR, 'body > book-app > app-header > app-toolbar')

# Access the Shadow DOM
button_inside_shadow = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'button')),
    message="Button not found within Shadow DOM"
)

# Click the button
button_inside_shadow.click()

time.sleep(10)

driver.quit()
