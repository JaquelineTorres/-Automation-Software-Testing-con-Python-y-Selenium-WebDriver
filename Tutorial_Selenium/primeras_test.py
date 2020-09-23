import unittest

class Operations(unittest.TestCase):

    def test_sum(self):
        sum = 1 + 1
        self.assertEqual(sum, 3, msg="El resultado de la suma es invalido")

    def test_sub(self):
        sub = 1 - 1
        self.assertNotEqual(sub, 2)

    def test_isupper(self):
        self.assertTrue('COURSE'.isupper())
        self.assertFalse('course'.isupper())

if __name__ == '__main__':
    unittest.main()
