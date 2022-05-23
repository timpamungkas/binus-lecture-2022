import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator(200, 4)

    def test_addition(self):
        self.assertEqual(self.calculator.addition(), 204)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(), 196)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(), 800)

    def test_division(self):
        self.assertEqual(self.calculator.division(), 50)

if __name__ == "__main__":
    unittest.main()