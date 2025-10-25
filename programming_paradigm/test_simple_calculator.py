import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -8), -9)
        self.assertEqual(self.calc.add(6, -8), -2)
        self.assertEqual(self.calc.add("10", "9"), "109")
        self.assertEqual(self.calc.add("-3", "-9"), "-3-9")
        with self.assertRaises(TypeError):
            self.calc.add(9, "4")
        # Add more assertions to thoroughly test the add method.

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(-4, 2), -6)
        self.assertEqual(self.calc.subtract(4, -2), 6)
        with self.assertRaises(TypeError):
            self.calc.subtract(10, "3")
        with self.assertRaises(TypeError):
            self.calc.subtract("5", "7")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(-4, 2), -8)
        self.assertEqual(self.calc.multiply(-6, -2), 12)
        self.assertEqual(self.calc.multiply("9", 2), "99")
        self.assertEqual(self.calc.multiply("-5", 3), "-5-5-5")
        self.assertEqual(self.calc.multiply("-5", -3), "")
        self.assertEqual(self.calc.multiply("9", -7), "")
        with self.assertRaises(TypeError):
            self.calc.subtract("10", "3")
        with self.assertRaises(TypeError):
            self.calc.subtract("-10", "3")
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertEqual(self.calc.divide(4, -2), -2)
        self.assertEqual(self.calc.divide(-18, -2), 9)
        with self.assertRaises(TypeError):
            self.calc.subtract(10, "3")
        with self.assertRaises(TypeError):
            self.calc.subtract("5", "7")
        self.assertEqual(self.calc.divide(-2, 0), None)