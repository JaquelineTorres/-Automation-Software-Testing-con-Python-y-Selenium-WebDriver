from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/#")
#driver.maximize_window()

alert_button = driver.find_element_by_xpath("//button[@onclick='myFunction()']")
alert_button.click()

time.sleep(5)
# esta fn permite dar click en el boton "aceptar" de la alerta
#driver.switch_to_alert().accept()

# esta fn permite dar click en el boton "calcelar" de la alerta

driver.switch_to_alert().dismiss()
#driver.quit()