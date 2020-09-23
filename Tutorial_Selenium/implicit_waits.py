from selenium import webdriver
import unittest
class ImplicitWaits(unittest.TestCase):
    def setUp(self):# setUp se ejecuta primero antes de las demás pruebas
        # Precondiciones:
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=90)
        #espera un tiempo determinado de espera, espera 90 segundos
        #espera 90 segundo en cada una de las pruebas
        # Pero esta implicitly_wait hace más lenta la prueba
    def test_login_page(self):
        # Title da a conocer el nombre de la pag. principal
        title_login_page = self.driver.title
        self.assertEqual(title_login_page, "OrangeHRM")
    def test_validate_login(self):
        username = self.driver.find_element_by_id("txtUsername")
        password = self.driver.find_element_by_id("txtPassword")
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn = self.driver.find_element_by_id("btnLogin")
        login_btn.click()
        main_menu = self.driver.find_element_by_class_name("menu")
        # Esta arroga True o False, debe de arrogar True, esto indica que hizo
        # el login correctamente
        self.assertTrue(main_menu.is_displayed(), msg="El login no se realiza de manera satisfaxctoria")
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()


