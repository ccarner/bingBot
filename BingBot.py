from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def searchNews(driver):
    element = driver.find_element_by_id("scp14").click()

def normalSearch(driver):
    driver.get("http://bing.com")
    assert "Bing" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()

    # between 1 and 3 chars in search box
    for i in range(1,random.randint(0,3)): 
        elem.send_keys( chr(random.randint(ord('A'),ord('z'))))
    
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.RETURN)
    
    #assert "No results found." not in driver.page_source

def Main():
    driver=webdriver.Chrome("./drivers/chromedriver.exe")
    normalSearch(driver)
    #driver.close()    

Main()





