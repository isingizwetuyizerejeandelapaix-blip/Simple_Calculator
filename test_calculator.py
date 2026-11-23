"""Automated checks for the calculator's arithmetic and input handling."""

import unittest

from calculator import (
    addition,
    calculate_result,
    division,
    format_result,
    multiplication,
    subtraction,
)


class CalculatorTests(unittest.TestCase):
    def test_four_arithmetic_functions(self):
        self.assertEqual(addition(50, 20), 70)
        self.assertEqual(subtraction(50, 20), 30)
        self.assertEqual(multiplication(5, 4), 20)
        self.assertEqual(division(100, 5), 20)

    def test_operation_selection_uses_two_inputs(self):
        self.assertEqual(calculate_result("Addition (+)", "50", "20"), 70)
        self.assertEqual(
            calculate_result("Subtraction (-)", "50", "20"), 30
        )
        self.assertEqual(
            calculate_result("Multiplication (×)", "5", "4"), 20
        )
        self.assertEqual(calculate_result("Division (÷)", "100", "5"), 20)

    def test_division_by_zero_returns_clear_error(self):
        message = "Error: Cannot divide by zero!"
        self.assertEqual(division(50, 0), message)
        self.assertEqual(calculate_result("Division (÷)", "50", "0"), message)
        self.assertEqual(format_result(message), message)

    def test_non_numeric_input_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_result("Addition (+)", "hello", "20")

    def test_unknown_operation_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "valid operation"):
            calculate_result("Power", "2", "3")


if __name__ == "__main__":
    unittest.main()
