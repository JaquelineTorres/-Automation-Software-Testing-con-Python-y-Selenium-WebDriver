from selenium import webdriver
import unittest
import HtmlTestRunner
class HtmlreportsLogin(unittest.TestCase):
    def setUp(self):
        # Precodition:
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
    def test_login_page(self):
        title_login_page = self.driver.title
        self.assertEqual(title_login_page, "OrangeHRM345")
    def test_validate_login(self):
        username = self.driver.find_element_by_id("txtUsername")
        password = self.driver.find_element_by_id("txtPassword")
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn = self.driver.find_element_by_id("btnLogin")
        login_btn.click()
        main_menu = self.driver.find_element_by_class_name("menu")
        self.assertTrue(main_menu.is_displayed())
    def tearDown(self):
        self.driver.quit()
if __name__== '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='\\Users\\jaque\\PycharmProjects\\Tutorial_Selenium\\reports'))




