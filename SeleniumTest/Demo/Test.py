from Selenium import webdriver  
import time  
from Selenium.webdriver.common.keys import Keys  
print("test case started")  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.delete_all_cookies()  
driver.get("https://www.gmail.com")  
driver.find_element_by_id("identifierId").send_keys("imanazahari99@gmail.com")  
time.sleep(2)  
driver.find_element_by_xpath("//span[@class='RveJvd snByac'][1]").click()  
time.sleep(3)  
driver.find_element_by_name("password").send_keys("************")  
time.sleep(3)  
driver.find_element_by_xpath("//span[contains(text(),'Next')][1]").click()  
time.sleep(3)  
driver.close()  
print("Gmail login has been successfully completed")  