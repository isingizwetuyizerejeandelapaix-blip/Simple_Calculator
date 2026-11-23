# Simple Calculator

A graphical calculator built with Python and Tkinter for the Codveda Technologies Python Development Internship, Level 1.

## Features

- Addition, subtraction, multiplication, and division
- Two number fields and a menu for selecting an operation
- Division-by-zero handling with a clear message
- Validation for non-numeric input
- A simple graphical interface with keyboard support

## Requirements

- Python 3 with Tkinter
- No third-party packages

## Run the calculator

From this folder, run:

```bash
python3 calculator.py
```

Enter two numbers, choose an operation, then select **Calculate**. Pressing Return also calculates.

## Run the tests

The test suite checks all four arithmetic functions, operation selection, two-input handling, invalid input, and division by zero:

```bash
python3 -m unittest -v
```

## Project structure

```text
Simple_Calculator/
├── calculator.py
├── test_calculator.py
├── README.md
└── screenshots/
```

## Internship details

- Organization: Codveda Technologies
- Position: Python Development Intern
- Level: 1 - Basic
- Task: Simple Calculator
