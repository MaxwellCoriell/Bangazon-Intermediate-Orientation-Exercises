import unittest
from calculator import *

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        # Create an instance of the calculator that can be used in all tests
        self.casio = Calculator()

    def test_add(self):
        self.assertEqual(self.casio.add(2, 7), 9)

    # Write test methods for subtract, multiply, and divide
    
    def test_subtract(self):
        self.assertEqual(self.casio.subtract(2, 7), -5)

    def test_multiply(self):
        self.assertEqual(self.casio.multiply(2, 7), 14)

    def test_divide(self):
        self.assertAlmostEqual(self.casio.divide(2, 7), 0.2857, places=4)

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

if __name__ == '__main__':
    unittest.main()