from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(1)

username = driver.find_element_by_css_selector("input#txtUsername")
username.send_keys("admin")

password = driver.find_element_by_css_selector("input#txtPassword")
password.send_keys("admin123")
time.sleep(1)

btn_login = driver.find_element_by_css_selector("input.button")
btn_login.click()