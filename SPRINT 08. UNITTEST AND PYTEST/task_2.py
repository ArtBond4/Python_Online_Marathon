import unittest

class DivideTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(divide(5, 5), 1)

    def test_2(self):
        self.assertEqual(divide(10, 5), 2)

    def test_3(self):
        self.assertEqual(divide(100, 10), 10)
