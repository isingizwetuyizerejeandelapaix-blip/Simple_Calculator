"""Automated checks for the calculator's arithmetic and command-line flow."""

import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from calculator import (
    addition,
    calculator,
    division,
    multiplication,
    subtraction,
)


class CalculatorTests(unittest.TestCase):
    def test_four_arithmetic_operations(self):
        self.assertEqual(addition(50, 20), 70)
        self.assertEqual(subtraction(50, 20), 30)
        self.assertEqual(multiplication(5, 4), 20)
        self.assertEqual(division(100, 5), 20)

    def test_division_by_zero_returns_clear_error(self):
        self.assertEqual(division(50, 0), "Error: Cannot divide by zero!")

    def test_menu_rejects_invalid_choice_and_number_then_calculates(self):
        answers = ["8", "1", "hello", "50", "20", "5"]
        output = StringIO()

        with patch("builtins.input", side_effect=answers) as mocked_input:
            with redirect_stdout(output):
                calculator()

        self.assertEqual(mocked_input.call_count, 6)
        self.assertEqual(
            [entry.args[0] for entry in mocked_input.call_args_list],
            [
                "Select an operation (1-5): ",
                "Select an operation (1-5): ",
                "Enter first number: ",
                "Enter first number: ",
                "Enter second number: ",
                "Select an operation (1-5): ",
            ],
        )
        self.assertIn("Invalid choice! Please select 1-5.", output.getvalue())
        self.assertIn("Invalid input! Please enter a number.", output.getvalue())
        self.assertIn("Result: 70.0", output.getvalue())

    def test_menu_handles_division_by_zero_and_exits(self):
        answers = ["4", "50", "0", "5"]
        output = StringIO()

        with patch("builtins.input", side_effect=answers):
            with redirect_stdout(output):
                calculator()

        self.assertIn("Result: Error: Cannot divide by zero!", output.getvalue())
        self.assertIn("Thank you for using Python Calculator!", output.getvalue())


if __name__ == "__main__":
    unittest.main()
