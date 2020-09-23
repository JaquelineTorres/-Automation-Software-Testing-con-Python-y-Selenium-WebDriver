from selenium import webdriver

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

# Maximiza ventana
driver.maximize_window()

driver.get("file:///Users/jaque/Desktop/web/table_curso_Automation.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/td"))

print(rows)
print(cols)

print("Company" + "      " + "Contact" + "     " + "Country")

for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(value, end='      ')
    print()
