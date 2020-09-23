from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(1)
username = driver.find_element_by_css_selector("input[name='txtUsername']")
username.send_keys("Admin")

password = driver.find_element_by_css_selector("input[id='txtPassword']")
password.send_keys("admin123")
time.sleep(1)

botton_login = driver.find_element_by_css_selector("input[class='button']")
botton_login.click()

time.sleep(1)
