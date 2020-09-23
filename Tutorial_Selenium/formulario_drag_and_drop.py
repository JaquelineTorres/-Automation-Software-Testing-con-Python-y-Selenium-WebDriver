from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#driver.maximize_window()

source_element_1 = driver.find_element_by_id("box3")
target_element_1 = driver.find_element_by_id("box103")

source_element_2 = driver.find_element_by_id("box6")
target_element_2 = driver.find_element_by_id("box106")

action_chains = ActionChains(driver)

action_chains.drag_and_drop(source = source_element_1,target = target_element_1).perform()
action_chains.drag_and_drop(source = source_element_2,target = target_element_2).perform()

time.sleep(3)
driver.quit()
