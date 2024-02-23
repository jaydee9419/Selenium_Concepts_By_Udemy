"""
Headless
---------------
tasting will going on backend and we are unable to see the brower action in visable
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

options = Options()
options.add_argument("--headless=new")


driver = webdriver.Chrome(options=options)
# driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

webpage_title = driver.title

print("webpage Title is: ",webpage_title)
print("webpage url is: ",driver.current_url)

time.sleep(2)







