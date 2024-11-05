from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

#-- Chrome
from  selenium.webdriver.common.by import By

import time


#"C:\Users\NCTV_User_002\Documents\chromedriver-win64\chromedriver.exe"
service_obj = Service("/Users/NCTV_User_002/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#Maximize to fullscreen
driver.maximize_window()
