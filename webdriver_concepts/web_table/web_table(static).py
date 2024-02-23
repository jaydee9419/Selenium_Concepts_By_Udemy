"""
webtable
-------------
1. Static webtable
2. dynamic webtable


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")


# 1. count no of rows and columns
# ----------------------------------------
# locating the table rows
table_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
# count no of rows
print("No of Rows: ", table_rows)

# locating the table columns
table_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[2]/td"))
# count no of columns
print("No of Columns: ", table_columns)
print("=================================================================================================")


# 2. read specific row and column data required: (row 3 and column 2)
# ----------------------------------------
# locating the table specific column and row
table_specific_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[3]/td[2]")
print(table_specific_data.text)
print("=================================================================================================")


# 3. read all the table data dynamically
# ----------------------------------------
for row in range(2, table_rows + 1):
    for column in range(1, table_columns + 1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(row) + "]/td[" + str(column) + "]")
        print(data.text, end="          ")
    print(" ")
print("=================================================================================================")        


# 4. read data based on conditions(list books name whose author is mukesh)
# ----------------------------------------       
for row in range(2, table_rows + 1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if author == 'Mukesh':
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[4]").text
        print(f"Author is: {author}   Written Books: {bookname}    Price: {price}") 
          
print("=================================================================================================")

time.sleep(5)
driver.quit()

