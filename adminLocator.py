from itertools import count
from operator import index

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC

#-- Chrome
from  selenium.webdriver.common.by import By

import time

from selenium.webdriver.common.devtools.v85.log import clear
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait




#"C:\Users\NCTV_User_002\Documents\chromedriver-win64\chromedriver.exe"
service_obj = Service("/Users/NCTV_User_002/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#Maximize to fullscreen
driver.maximize_window()
# Website to get to login the dashboard
driver.get("https://dev-dashboard.n-compass.online/")



driver.implicitly_wait(60)



# ADMIN ACCOUNT
email = "johnmichael@admin.com"
password = "password"



def clearText(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((attr, value))
    )
    element.clear()


def inputText(attr, value, text):
    clearText(attr, value)

    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((attr, value))
    )
    element.send_keys(text)


def clickButton(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((attr, value))
    )
    element.click()


def clearButton(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((attr, value))
    )
    element.click()


def closeButton(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((attr, value))
    )
    element.click()

def selectField(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((attr, value))
    )
    element.click()

def clickDDCheckBox(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((attr, value))
    )
    element.click()

def textField(attr, value):
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((attr, value))
    )
    return element.text


def Login():

    # Enter email
    inputText(By.XPATH, "//input[@id='mat-input-0']", email)
    # Enter password
    inputText(By.XPATH, "//input[@id='mat-input-1']", password)
    # Click to see password
    clickButton(By.CSS_SELECTOR, "mat-icon[role='img']")
    # Click to LOGIN
    clickButton(By.XPATH, "//button[@type='submit']")
    # Close the Welcome Modal
    closeButton(By.XPATH, "//button[normalize-space()='Close']")

# Loging in
Login()


def navLocator():
    clickButton(By.XPATH, "//a[@ng-reflect-router-link='locator']")

# Navigate to Locator page
navLocator()
dealer_call_count = 0
#def selectDealerName():

 #   selectField(By.XPATH, "(//div[@class='mat-form-field-infix'])[1]")

#selectDealerName()

def getSelectedDealerName(index):
    # Get the selected dealer's name from the dropdown or displayed section
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"(//mat-option/span/div[@class='dealer md-text'])[{index}]"))
    ).text

# Dealer Name i choose
dealerName = ["Horse Bet Racing", "BomboClat Clothes", "Rainbow"]

def clickDealerName():
    #global dealer_call_count
    #dealer_call_count += 1

    ge = driver.find_element(By.XPATH, "(//div[@class='mat-form-field-infix'])[1]")
    ge.click()

    #clickDDCheckBox(By.XPATH, f"//mat-option[@ng-reflect-value='[object Object]'][{index}]")
    dealerNameDropdown = driver.find_elements(By.XPATH, "//mat-option[@role='option']")
    for dealer in dealerNameDropdown:
        if dealer.text in dealerName:
            dealer.click()

            break  # Move to the next dealer name


    #selected_dealer = getSelectedDealerName(index)
    #print(f"Selected Dealers Nmae: {selected_dealer}")
    #assert selected_dealer in dealerName


clickDealerName()




time.sleep(10)

#selectDealerName.select_by_visible_text("Salt Bae")


#(//mat-pseudo-checkbox[@class='mat-option-pseudo-checkbox mat-pseudo-checkbox ng-star-inserted'])[1]

# //mat-option[@ng-reflect-value='[object Object]']
# name inside of the accordion
# //mat-option[@ng-reflect-value='[object Object]']/span/div