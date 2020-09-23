from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/")
#driver.maximize_window()

#cambia el foco al primer frame
driver.switch_to.frame("packageListFrame")
link_frame_1 = driver.find_element_by_link_text("com.thoughtworks.selenium")
link_frame_1.click()
time.sleep(3)

#Cambia el foco al marco predeterminado
driver.switch_to.default_content()

#cambia el foco al segundo frame
driver.switch_to.frame("packageFrame")
link_frame_2 = driver.find_element_by_link_text("CommandProcessor")
link_frame_2.click()
time.sleep(3)

#Cambia el foco al marco predeterminado
driver.switch_to.default_content()

#cambia el foco al tercer frame
driver.switch_to.frame("classFrame")
link_frame_3 = driver.find_element_by_xpath("/html/body/div[1]/ul/li[7]/a")
link_frame_3.click()
time.sleep(3)

#Cambia el foco al marco predeterminado
driver.switch_to.default_content()

# Salir del driver
driver.quit()