"""A simple command-line calculator for the Codveda Python internship."""


def addition(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtraction(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiplication(a, b):
    """Return the product of two numbers."""
    return a * b


def division(a, b):
    """Return the quotient, or an error message when b is zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def get_number(message):
    """Prompt until the user enters a valid number."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    """Run the calculator menu until the user chooses to exit."""
    operations = {
        "1": ("Addition (+)", addition),
        "2": ("Subtraction (-)", subtraction),
        "3": ("Multiplication (*)", multiplication),
        "4": ("Division (/)", division),
    }

    while True:
        print("\n================================")
        print("       PYTHON CALCULATOR")
        print("================================")
        for choice, (label, _) in operations.items():
            print(f"{choice}. {label}")
        print("5. Exit")
        print("================================")

        choice = input("Select an operation (1-5): ").strip()

        if choice == "5":
            print("\nThank you for using Python Calculator!")
            break

        if choice not in operations:
            print("Invalid choice! Please select 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        _, operation = operations[choice]
        result = operation(num1, num2)

        print("\n--------------------------------")
        print("Result:", result)
        print("--------------------------------")


if __name__ == "__main__":
    calculator()
