from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
#driver.maximize_window()
# Loging
username = driver.find_element(By.NAME, "txtUsername")
username.send_keys("admin")
password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("admin123")
time.sleep(1)
login = driver.find_element(By.ID, "btnLogin")
login.click()

# PIM
pim_menu = driver.find_element_by_id("menu_pim_viewPimModule")
pim_menu.click()

time.sleep(3)

conf_menu = driver.find_element_by_id("menu_pim_Configuration")
conf_menu.click()

time.sleep(3)

option_fields =  driver.find_element_by_id("menu_pim_configurePim")
option_fields.click()

list_checkBox= driver.find_elements_by_css_selector("li[class='checkbox']>input")

edit_botton = driver.find_element_by_id("btnSave")

for checkBox in list_checkBox:
    if checkBox.is_displayed() is True and checkBox.is_enabled() is False:
        edit_botton.click()
        time.sleep(3)
    if checkBox.is_displayed() is True and checkBox.is_selected() is False:
        time.sleep(3)
        checkBox.click()
    else:
        checkBox.click()
edit_botton.click()

# matar la istancia de driver
driver.quit()


