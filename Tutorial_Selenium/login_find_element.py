from selenium import webdriver
from selenium.webdriver.common.by import By
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

time.sleep(1)
## localiza el texto, debe estar completo
link_1 = driver.find_element(By.LINK_TEXT, "Welcome Linda")
link_1.click()

time.sleep(1)
## Esta función localiza el texto Lougout, texto que queires que haga click, puede no estar completo
link_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
link_2.click()

driver.quit()