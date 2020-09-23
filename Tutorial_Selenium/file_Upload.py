from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

#driver.maximize_window()

#el boton de Choose Files se encuntra dentro de un Frame, es por eso que
# debemos de decirle que se enfoque en el frame que contiene este boton
driver.switch_to_frame("frame-one1434677811")

file_upload_btn = driver.find_element_by_id("RESULT_FileUpload-10")
time.sleep(5)
# Ruta del umagen a subir
file_upload_btn.send_keys("/Users/jaque/Downloads/Screen Shot 2020-09-21 at 23.36.11.png")
