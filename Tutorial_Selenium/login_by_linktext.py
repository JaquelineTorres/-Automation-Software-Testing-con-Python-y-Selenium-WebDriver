from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(1)
link_reset_password=driver.find_element_by_partial_link_text("Forgot")
link_reset_password.click()
time.sleep(1)
