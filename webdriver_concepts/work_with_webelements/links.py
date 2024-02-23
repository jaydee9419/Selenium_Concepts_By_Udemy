"""
Links
---------------------------
---------------------------
1. internal 
2. External
3. Broken

---------------------------
1. internal Links
- navigate to same page   

2. external link
- navigate to target page (go to some other page)

3. broken link
- will not have any target page or location (Developers will addd these for future adding)

"""

#-------------------------------------------------
                #both external and internal links
#-------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://omayo.blogspot.com/")

print(driver.current_url)

# #open the header
# blogs = driver.find_element(By.ID, "blogsmenu")
# blogs.click()
# time.sleep(3)

# #caling inside header link
# selenium143 = driver.find_element(By.LINK_TEXT, "Selenium143")
# selenium143.click()


# how to find no of links in a page

#by using TAG_NAME
# links = driver.find_elements(By.TAG_NAME, 'a')

# #By using XPATH
# links = driver.find_elements(By.XPATH, "//a")
# print("Total no of links: ", len(links))

# #print all the links
# for each_link in links:
#     print(each_link.text)



#--------------------------------------------------------
                    #broken links
#--------------------------------------------------------



time.sleep(5)
driver.quit()