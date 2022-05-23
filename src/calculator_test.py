import unittest
from src.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.calculator = Calculator(125, 5)

    def test_addition(self):
        self.assertEqual(self.calculator.addition(), 130)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(), 120)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(), 625)

    def test_division(self):
        self.assertEqual(self.calculator.division(), 25)

if __name__ == "__main__":
    unittest.main()