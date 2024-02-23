                                    #Selenium3
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set the path to the EdgeDriver executable
# edge_path = r'D:\Work_Environment\Python\Udemy\Selenium_Python\msedgedriver.exe'

# # Create EdgeOptions and set the path
# edge_options = webdriver.EdgeOptions()
# edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'  # Adjust the path as needed
# edge_options.add_argument("start-maximized")  # Optional: maximize the browser window

# # Create EdgeService and pass EdgeOptions
# edge_service = EdgeService(executable_path=edge_path)

# # Create the Edge WebDriver
# driver = webdriver.Edge(service=edge_service, options=edge_options)

# # Navigate to the OrangeHRM website
# driver.get("https://opensource-demo.orangehrmlive.com/")

# # Wait for the username field to be present
# uname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "txtUsername")))
# uname.send_keys("Admin")

# # Wait for the password field to be present
# upass = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'txtPassword')))
# upass.send_keys('admin.123')

# # Wait for the login button to be clickable and click it
# login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btnLogin')))
# login_button.click()

# # You may add more steps here based on your workflow

# # Quit the WebDriver
# driver.quit()



                                    #Selenium - 4


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
# path = Service(r'D:\Work_Environment\Python\Udemy\Selenium_Python\msedgedriver.exe')
driver = webdriver.Edge()
# driver = webdriver.Edge(service=path)

driver.get("https://opensource-demo.orangehrmlive.com/")


driver.maximize_window()
time.sleep(10)
# Perform actions on the website if needed
driver.find_element(By.NAME, 'username').send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys('admin123')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# Close the entire browser, including all windows/tabs

time.sleep(10)

web_title = driver.title

print(web_title)
exp_title = "OrangeHRM"

if web_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
    
    
driver.quit()

