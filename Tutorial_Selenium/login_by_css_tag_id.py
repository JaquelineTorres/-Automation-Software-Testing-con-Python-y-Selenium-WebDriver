from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

username = driver.find_element_by_css_selector("input#txtUsername")
username.send_keys("Admin")

time.sleep(1)

password = driver.find_element_by_css_selector("input#txtPassword")
password.send_keys("admin123")

login = driver.find_element_by_css_selector("input#btnLogin")
login.click()

time.sleep(1)