from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")


#login
uname = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
uname.send_keys("Admin")

password = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
password.send_keys("admin123")

submit = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
submit.click()

# Total rows in a table
table = len(driver.find_elements(By.XPATH , "//div[@class='oxd-table-body']/div"))
print(table)

count = 0
for row in range(1, table + 1):
    status = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div["+str(row)+"]/div/div[5]").text
    # print(status)
    if status == "Disabled":
        count +=1
print(f"Total no of users: {row}")
print(f"Total nop of Enabled users: {row - count}")
print(f"Total nop of Disabled users: {count}")






time.sleep(5)
driver.quit()