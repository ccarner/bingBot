from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import time

# for sending keys one by one, with a gap!
def send_keys_delay_random(elem,keys,min_delay=0.05,max_delay=0.25):
    for key in keys:
        elem.send_keys(key)
        time.sleep(random.uniform(min_delay,max_delay))

def searchNews(driver):
    #incomplete
    element = driver.find_element_by_id("scp14").click()

def normalSearch(driver):
    driver.get("http://bing.com")
    assert "Bing" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()

    # between 1 and 2 chars in search box
    for i in range(random.randint(1,2)): 
        elem.send_keys( chr(random.randint(ord('a'),ord('z'))))
        time.sleep(random.uniform(0.1,0.3))

    #between 1 and 5 down arrow presses chars in search box
    for i in range(random.randint(1,5)): 
        elem.send_keys(Keys.ARROW_DOWN)
        time.sleep(random.uniform(0.1,0.3))
    
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    
    #assert "No results found." not in driver.page_source

def login(driver):
    driver.get("http://bing.com")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="id_s"]').click() #click the signin button on homepage
    time.sleep(5)
    elem = driver.find_element_by_xpath('//*[@id="i0116"]') #select the email textbox element
    send_keys_delay_random(elem, "alexdadder1@yahoo.com") # type out values 'semi realistically' using custom func
    time.sleep(5)
    elem.send_keys(Keys.RETURN) # move to next screen
    time.sleep(5)
    elem = driver.find_element_by_xpath('//*[@id="i0118"]') #select the password textbox element
    send_keys_delay_random(elem, "MicrosoftPassword")
    time.sleep(1)
    elem.send_keys(Keys.RETURN) # move to next screen
    time.sleep(3)

def Main():
    chrome_options = Options()  
    # for running chrome without a window?
    #chrome_options.add_argument("--headless --disable-gpu")  
    driver=webdriver.Chrome(executable_path ="./drivers/chromedriver.exe", chrome_options = chrome_options)
    driver.set_window_position(2000,0)
    login(driver)
    for i in range (0,10):
        normalSearch(driver)
        time.sleep(random.uniform(5,20))
    time.sleep(10)
    #driver.close()    

#run the damn program already!
Main()





