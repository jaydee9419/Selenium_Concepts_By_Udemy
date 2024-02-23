"""
browser window
----------------

.switch_to.window(WindowID)
single_WindowID = .current_window_handle - gives us WindowID of single browser window 
all_windowsID = window.handles - this will return window id's of multiple browser windows


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print("before clicking the link: ",driver.window_handles)


home_link = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")
home_link.click()

window_ids = driver.window_handles

# #approach - 1 individual identification by idex number
# print(f"Parant window ID: {window_ids[0]}")
# print(f"Child window ID: {window_ids[1]}")

# main_window = window_ids[0]
# Child_window = window_ids[1]

# driver.switch_to.window(Child_window)
# print(driver.title)
# print(driver.current_url)

# time.sleep(3)

# driver.switch_to.window(main_window)
# print(driver.title)
# print(driver.current_url) 


# approach - 2 - looping windows

# for win_id in window_ids:
#     driver.switch_to.window(win_id)
#     print(driver.title)
#     print(driver.current_url)

# apprtoach - 3 i want to close one window based on my choice
for win_id in window_ids:
    driver.switch_to.window(win_id)
    if driver.title == 'OrangeHRM HR Software | OrangeHRM' and driver.title == 'OrangeHRM':
        driver.close()
    


time.sleep(5)
driver.quit()

