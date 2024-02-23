"""
mouse operations
====================
there is a class: ActionChains()

under this calss we have follwing options
- Mouse hover   - move_to_element(element)
- Right click   - context_click(element).perform()
- Double click  - double_click(element).perform()
- Drag and Drop - drag_and_drop(source_element, taaget_element).perform()
- slide         - drag_and_drop_by_offset(element, X_axisvalue, Y_axisvalue)

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# # 1 Mouse Hover
# # ----------------------------------------------------------
# driver.get('https://omayo.blogspot.com/')

# blog = driver.find_element(By.XPATH, "//span[@id='blogsmenu']")
# selenium_143 = driver.find_element(By.LINK_TEXT, "Selenium143")



# action = ActionChains(driver)
# time.sleep(3)

# action.move_to_element(blog)
# time.sleep(10)

# action.move_to_element(selenium_143).click().perform()
# time.sleep(3)

# time.sleep(10)
# driver.quit()


# 2 right click
# ----------------------------------------------------------
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

button = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")

action = ActionChains(driver)

# rightclick action
action.context_click(button).perform()
time.sleep(2)

copy = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
copy.click()
time.sleep(2)

driver.switch_to.alert.accept()

time.sleep(10)
driver.quit()



# # 3 Double click
# # ----------------------------------------------------------
# driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3')

# driver.switch_to.frame("iframeResult")
# time.sleep(2)

# input1 = driver.find_element(By.XPATH, "//input[@id='field1']")
# input1.clear()
# time.sleep(2)
# input1.send_keys("Dileep")


# copy_button = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction()']")
# actions = ActionChains(driver)
# actions.double_click(copy_button).perform()


# time.sleep(10)
# driver.quit()


# # 4 Drag and Drop
# # ----------------------------------------------------------
# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# actions = ActionChains(driver)


# washington = driver.find_element(By.XPATH, "//div[@id='box3']")
# usa = driver.find_element(By.XPATH, "//div[@id='box103']")
# actions.drag_and_drop(washington, usa).perform()
# time.sleep(1)

# rome = driver.find_element(By.XPATH, "//div[@id='box6']")
# italy = driver.find_element(By.XPATH, "//div[@id='box106']")
# actions.drag_and_drop(rome, italy).perform()
# time.sleep(1)

# seoul = driver.find_element(By.XPATH, "//div[@id='box5']")
# south_korea = driver.find_element(By.XPATH, "//div[@id='box105']")
# actions.drag_and_drop(seoul, south_korea).perform()
# time.sleep(1)

# oslo = driver.find_element(By.XPATH, "//div[@id='box1']")
# norway = driver.find_element(By.XPATH, "//div[@id='box101']")
# actions.drag_and_drop(oslo, norway).perform()
# time.sleep(1)

# madrid = driver.find_element(By.XPATH, "//div[@id='box7']")
# spain = driver.find_element(By.XPATH, "//div[@id='box107']")
# actions.drag_and_drop(madrid, spain).perform()
# time.sleep(1)

# copenhagen = driver.find_element(By.XPATH, "//div[@id='box4']")
# denmark = driver.find_element(By.XPATH, "//div[@id='box104']")
# actions.drag_and_drop(copenhagen, denmark).perform()
# time.sleep(1)

# stockholm = driver.find_element(By.XPATH, "//div[@id='box2']")
# sweden = driver.find_element(By.XPATH, "//div[@id='box102']")
# actions.drag_and_drop(stockholm, sweden).perform()
# time.sleep(1)

# time.sleep(10)
# driver.quit()


# # 4 Drag and Drop
# # ----------------------------------------------------------
# driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

# min = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
# max = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

# print("location of the slidebar in the webpage before sliding")
# print(min.location) # {'x': 59, 'y': 250}
# print(max.location) # {'x': 545, 'y': 250}

# # sliding based on location 
# actions = ActionChains(driver)

# actions.drag_and_drop_by_offset(min,100,0).perform()
# actions.drag_and_drop_by_offset(max,-100,0).perform()

# print("location of the slidebar in the webpage after sliding")
# print(min.location) # {'x': 161, 'y': 250}
# print(max.location) # {'x': 443, 'y': 250}

# time.sleep(6)
# driver.quit()

# # 6. Scrolling page
# # -------------------------------------------------------
# """
# 3 options we have
# - based on pixel number
# - till elemnet found
# - from top to bottom
# """
# driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# # # Scroll down the page by pixel number
# # driver.execute_script("window.scrollBy(0,3000)","")
# # value = driver.execute_script("return window.pageYOffset")
# # print(f"No of pixels moved: {value}")

# # # Scroll down page till the element is visable
# # india = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]")
# # driver.execute_script("arguments[0].scrollIntoView();", india)
# # value = driver.execute_script("return window.pageYOffset")
# # print(f"No of pixels moved: {value}")

# # scroll down the page till end of the page
# #top to bottom
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset")
# print(f"No of pixels moved: {value}")

# time.sleep(2)
# #Bottom to top
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
# value = driver.execute_script("return window.pageYOffset")
# print(f"No of pixels moved: {value}")

# time.sleep(6)
# driver.quit()