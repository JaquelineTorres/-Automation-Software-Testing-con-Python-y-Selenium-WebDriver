from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

link_orange = driver.find_element_by_partial_link_text("Orange")
link_orange.click()

print(driver.current_window_handle)#CDwindow-7E8D21F97FBE3FD8BDFCE6296F9E10C3

#retona todos los valores handle de las ventanas abirtas dek navegador
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "OrangeHRM":## Nombre de la primera ventana
        driver.close()##solamente cierra la ventana actual, o en la que nos encontremos

driver.quit()## elimina toda la intancia de webdriver/ cierraTODO


