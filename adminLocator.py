from itertools import count

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC

#-- Chrome
from  selenium.webdriver.common.by import By

import time

from selenium.webdriver.common.devtools.v85.log import clear
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#"C:\Users\NCTV_User_002\Documents\chromedriver-win64\chromedriver.exe"
service_obj = Service("/Users/NCTV_User_002/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#Maximize to fullscreen
driver.maximize_window()
time.sleep(2)

#Website to get to login the dashboard
driver.get("https://dev-dashboard.n-compass.online/")

# ADMIN ACCOUNT
email = "johnmichael@admin.com"
password = "password"

# Input Email Address
#driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys(email)
#time.sleep(2)

EmailAdd = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='mat-input-0']")))
EmailAdd.send_keys(email)

PassInput = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@id='mat-input-1']")
    )
)

PassInput.send_keys(password)

# Input Password
#driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys(password)
#time.sleep(2)

# Click the password visibility to see password
driver.find_element(By.CSS_SELECTOR, "mat-icon[role='img']").click()
time.sleep(2)

# To login ADMIN account
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

# Close the Welcome Modal
driver.find_element(By.XPATH, "//button[normalize-space()='Close']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[@ng-reflect-router-link='locator']").click()
time.sleep(20)

driver.find_element(By.XPATH, "(//div[@class='mat-form-field-infix'])[1]").click()



#selectDealerName.select_by_visible_text("Salt Bae")
time.sleep(2)

time.sleep(5)



# //mat-option[@ng-reflect-value='[object Object]']

# //mat-option[@ng-reflect-value='[object Object]']/span/div