from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(1)
username=driver.find_element_by_name("txtUsername")
username.send_keys("Admin")

time.sleep(1)
password=driver.find_element_by_name("txtPassword")
password.send_keys("admin123")

login_btn=driver.find_element_by_name("Submit")
login_btn.click()


driver.close()