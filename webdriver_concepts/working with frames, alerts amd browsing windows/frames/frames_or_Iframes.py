"""
frames/Iframes representing tag name in html as follows
- frame
- iframe
- form
-------------------------
- we can not access another frame  from one frame if we are alredy in one frame
- if we are in one frame need to switch default content and switch to another

default/main page = .switch_to.default_content()
"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.maximize_window()

# # # we will get en authontication popup
# # driver.get("https://the-internet.herokuapp.com/digest_auth")

# # we need to pass username and password to buypass the alert/popup
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")


# ## to be write code

# time.sleep(5)
# driver.quit()



"""
frames/Iframes
-------------------------
once we open the browser we need to switch to the required frame
by usng the follwing methods:
------------------------------
python - 3
------------
switch_to_frame()

python - 4
------------
1. switch_to.frame(name of the frame)
2. switch_to.frame(id of the frame)
3. switch_to.frame(web element)
4. switch_to.frame(0) #if we have only one frame we can use index like 0

intraftion another frame from one frame
--------------------------------------------
- we can not access another frame  from one frame if we are alredy in one frame
- if we are in one frame need to switch default content and switch to another

default/main page = .switch_to.default_content()
"""

from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

# # we will get en authontication popup
# driver.get("https://the-internet.herokuapp.com/digest_auth")

# we need to pass username and password to buypass the alert/popup
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(1)

#clicking the Iframe with in an Iframe link on the web page
dual_frame = driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe')
dual_frame.click()
time.sleep(2)

#finding the main/outer frame
main_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")

#switching into the frame
driver.switch_to.frame(main_frame)

#finding the inner/sub frame
inner_frame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")

#switching into the frame
driver.switch_to.frame(inner_frame)

#finding search box
search_box = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')

#sending input to the search box
search_box.send_keys("Hello")
time.sleep(2)

# back to outer/main frame
driver.switch_to.parent_frame()
time.sleep(2)

# back to Registration web page
driver.switch_to.default_content()
time.sleep(2)

#clicking singleframe link
single_frame_link = driver.find_element(By.LINK_TEXT, 'Single Iframe')
single_frame_link.click()

#calling frame
frame = driver.find_element(By.XPATH, "//iframe[@id='singleframe']")

#switching into the frame
driver.switch_to.frame(frame)
time.sleep(2)

#clicking input box in the frame
searchbox = driver.find_element(By.XPATH, "/html/body/section/div/div/div/input")
searchbox.send_keys("World")

# back to main web page
driver.switch_to.default_content()
time.sleep(2)

#again clicking the Iframe with in an Iframe link on the web page
dual_frame = driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe')
dual_frame.click()
 
time.sleep(5)
driver.quit()