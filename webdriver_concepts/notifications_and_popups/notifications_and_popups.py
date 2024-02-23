"""
options.add_argument("--disable-notifications")

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# to disable the notifications
options = Options()
options.add_argument("--disable-notifications")

# decide the browser along with above disable options
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

# calling the website
driver.get("https://whatmylocation.com/")




time.sleep(5)
driver.close()