"""
wait commands
------------------
------------------
- from python
----------------
time.sleep(time in seconds)
pros:   - simple to use
cons:   - performance will be reduced
        - if the element is not available with the time given, there is a change to getting exception
        

- from selenium
------------------
1. implicit wait
pros: - single statement
      - performnce will not be reduced (if element is there then within the time it procced to execute athe action and move on to the next action)

cons  - if the element is not available with the time given, there is a chance to getting exception

2. explicit wait 
explicit wait works on conditions not on time
pros: - more effectivly works
       
cons  - need to insert in multiple places
      - user feels difficulty




----------------------------------------
1. implicat wait

"""
#----------------------------------------
#           implicit wait
#----------------------------------------

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://www.google.com/")

# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("selenium")
# search_box.submit()

# selenium = driver.find_element(By.XPATH, "//h3[text()='Selenium']")
# selenium.click()



#----------------------------------------
#           explicit wait
#----------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException,ElementNotSelectableException
driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10) #explicit wait declaration
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException, Exception]
                     ) #if we write Exception then no need to wrint every exception it means all exceptions will ignore

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")
search_box.submit()

selenium = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
selenium.click()















