from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

username = driver.find_element_by_xpath("//input[@name='txtUsername']")
username.send_keys("Admin")

time.sleep(1)

password = driver.find_element_by_xpath("//input[@name='txtPassword']")
password.send_keys("admin123")

time.sleep(1)
login = driver.find_element_by_xpath("//input[@type='submit']")
login.click()


