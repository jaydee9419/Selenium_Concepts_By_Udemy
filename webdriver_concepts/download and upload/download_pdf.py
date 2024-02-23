"""
Download file
====================

"""
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


# below 3 lines required to download files in desired location 
def Chrome_setup():
    # below 3 lines required to download files in desired location 
    """
    when i click download file, will open to same or another winodow instade of downloading Eg PDF file 
    How to overcome this?
    --------------------------
    add one more prefrence {"plugins.always_open_word_externally": True}
    """
  
    preferences = {"download.default_directory": "C:\\Users\\11571\\Downloads\\Docs", "plugins.always_open_pdf_externally": True}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preferences)
    
    driver = webdriver.Chrome(options=options)
    
    return driver

def Edge_setup():
    # below 3 lines required to download files in desired location 
    preferences = {"download.default_directory": "C:\\Users\\11571\\Downloads\\Docs"}
    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", preferences)
    
    driver = webdriver.Edge(options=options)
    
    return driver

def Firefox_setup():
    # below 3 lines required to popup window(ask to save file window) 
    options = webdriver.FirefoxOptions()
    """
    mime type - means "msword" dont ask save to download at the time of clicking download of msword format file
    Please follow the below lonk to find mime type files links 
    "https://www.sitepoint.com/mime-types-complete-list/"
    """
    options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/pdf")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    
    # Below lines required to set the prefered location to download
    """
    file will be downlad on 
    0 - Desktop
    1 - Download
    2 - desired location
    """
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser,download.dir", "C:\\Users\\11571\\Downloads\\Docs")
    """
    when i click download file, will open to same or another winodow instade of downloading Eg PDF file 
    How to overcome this?
    --------------------------
    add one more prefrence
    """
    options.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(options=options)
    
    return driver

# driver = Chrome_setup()
# driver = Edge_setup()
driver = Firefox_setup()




driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')


time.sleep(10)
file = driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a")
file.click()



time.sleep(20)
driver.quit()