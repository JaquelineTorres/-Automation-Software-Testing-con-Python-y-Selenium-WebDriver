import unittest
class MethodsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # Es ejecutado una vez la clase empieza
        print("SetUpClass-> Open Application")

    def setUp(self):
        print("setUp-> Login on Application")

    def test_create(self):
        print("Test create")

    def test_update(self):
        print("test update")

    def test_search(self):
        print("test search")

    def test_delete(self):
        print("test delete")

    def tearDown(self): # Es Ejecutado una vez la clase termina
        print("tearDown->Logout Application")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass-> Close Application")

if __name__ == '__main__':
    unittest.main()