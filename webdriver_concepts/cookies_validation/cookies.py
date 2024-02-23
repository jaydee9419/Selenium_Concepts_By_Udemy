"""
Cookies are the tempararry files which are created by the
browser at the time of browse websites

fowwing tasks we are doing 
---------------------------
- checking the chookies are created or not
- what type of cookies are created 
- extract the values of the cookies data
- we can delete all the cookies at a time 
- we can delete the specific cookie

"""
from webbrowser import Chrome
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

# #======================================================
# #capture all the cookies from the browser
# # - each cookies having miltiple attributies its kind of dictionary
# cookies = driver.get_cookies()
# print("size of cookies: ",len(cookies))
# print("-------------------------------------------")
# for item in cookies:
#     print(item)
#     print("-------------------------------------------")


# #===========================================================
# # if want to print any attibute value of the cookie
# cookies = driver.get_cookies()
# print("size of cookies: ",len(cookies))
# print("-------------------------------------------")
# for item in cookies:
#     print(item["value"],":",item["name"])
#     # or
#     print(item.get("name"),":",item.get("value"))
#     print("-------------------------------------------")


#===========================================================
# how to add a new cookie to the browser
driver.add_cookie({"name":"Jay Dee", "value":"9885514939"})
cookies = driver.get_cookies()
print("size of cookies: ",len(cookies))
print("-------------------------------------------")
for item in cookies:
    print(item["value"],":",item["name"])
    # or
    print(item.get("name"),":",item.get("value"))
    print("-------------------------------------------")


# #===========================================================
# # how to delete sepcific cookie from the browser
# driver.delete_cookie("Jay Dee")
# cookies = driver.get_cookies()
# print("size of cookies: ",len(cookies))
# print("-------------------------------------------")
# for item in cookies:
#     print(item["value"],":",item["name"])
#     # or
#     print(item.get("name"),":",item.get("value"))
#     print("-------------------------------------------")


#===========================================================
# how to delete all  cookies from the browser
# if stil having cookies then your browser/application is not allowing to do the deletion
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of cookies: ",len(cookies))
print("-------------------------------------------")
for item in cookies:
    print(item["value"],":",item["name"])
    # or
    print(item.get("name"),":",item.get("value"))
    print("-------------------------------------------")


time.sleep(5)
driver.quit()
