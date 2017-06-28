
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time


driver= webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.google.com/chrome/browser/desktop/index.html")


elm = driver.find_element_by_link_text('Download Chrome')
driver.implicitly_wait(5)
elm.click()
#driver.implicitly_wait(3)

elm1 = driver.find_element_by_id('eula-accept')
driver.implicitly_wait(3)
elm1.click()
time.sleep(8)
#driver.implicitly_wait(100)
#driver.get("chrome://downloads/")
#print ("reached here")
#elm2 = driver.find_element_by_id('save')

#driver.implicitly_wait(5)
#elm2.click()
pyautogui.click([367,942])
print ("clicked already")
driver.implicitly_wait(3)
pyautogui.click([103,954])
time.sleep(1)
pyautogui.click([693,517])
print ("installing  google chrome software")

