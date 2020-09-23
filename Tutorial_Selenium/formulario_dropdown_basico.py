from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
username = driver.find_element(By.NAME, "txtUsername")
username.send_keys("admin")
password = driver.find_element(By.XPATH,"//input[@type='password']")
password.send_keys("admin123")
time.sleep(1)
login = driver.find_element(By.ID, "btnLogin")
login.click()
admin_menu = driver.find_element_by_id("menu_admin_viewAdminModule")
admin_menu.click()
# Filtro
user_role_dropDown = Select(driver.find_element_by_id("searchSystemUser_userType"))
user_role_dropDown.select_by_index('2')
status_dropDown = Select(driver.find_element_by_id("searchSystemUser_status"))
status_dropDown.select_by_value('1')
#Esta función casi no se utiliza
#status_dropDown.select_by_visible_text("Enable")
search_btn = driver.find_element_by_id("searchBtn")
search_btn.click()
