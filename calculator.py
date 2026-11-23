"""A small Tkinter calculator for the Codveda Python internship."""

import tkinter as tk
from tkinter import ttk


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
    """Return the quotient, or a clear message when b is zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


OPERATIONS = {
    "Addition (+)": addition,
    "Subtraction (-)": subtraction,
    "Multiplication (×)": multiplication,
    "Division (÷)": division,
}


def calculate_result(operation, first_text, second_text):
    """Validate two text inputs and perform the selected operation."""
    first_number = float(first_text)
    second_number = float(second_text)

    try:
        selected_operation = OPERATIONS[operation]
    except KeyError as error:
        raise ValueError("Please select a valid operation.") from error

    return selected_operation(first_number, second_number)


def format_result(result):
    """Format numeric results without unnecessary trailing zeroes."""
    if isinstance(result, str):
        return result
    return f"{result:g}"


class CalculatorApp:
    """Build and run the calculator's graphical interface."""

    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator | Codveda")
        self.root.geometry("480x540")
        self.root.resizable(False, False)
        self.root.configure(bg="#F3F5F9")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#F3F5F9")
        style.configure(
            "Title.TLabel",
            background="#F3F5F9",
            foreground="#16213A",
            font=("Helvetica", 24, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background="#F3F5F9",
            foreground="#667085",
            font=("Helvetica", 11),
        )
        style.configure(
            "Field.TLabel",
            background="#FFFFFF",
            foreground="#344054",
            font=("Helvetica", 11, "bold"),
        )
        style.configure(
            "TEntry",
            padding=10,
            fieldbackground="#FFFFFF",
            font=("Helvetica", 13),
        )
        style.configure(
            "TCombobox",
            padding=9,
            fieldbackground="#FFFFFF",
            font=("Helvetica", 12),
        )
        style.configure(
            "Calculate.TButton",
            background="#315EFB",
            foreground="#FFFFFF",
            padding=(14, 12),
            font=("Helvetica", 12, "bold"),
        )
        style.map(
            "Calculate.TButton",
            background=[("active", "#244BDB"), ("pressed", "#1B3FC1")],
        )

        container = ttk.Frame(root, padding=(32, 30))
        container.pack(fill="both", expand=True)

        ttk.Label(container, text="Simple Calculator", style="Title.TLabel").pack(
            anchor="w"
        )
        ttk.Label(
            container,
            text="Codveda Technologies · Python Internship",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(6, 24))

        card = tk.Frame(
            container,
            bg="#FFFFFF",
            highlightbackground="#E4E7EC",
            highlightthickness=1,
            padx=22,
            pady=22,
        )
        card.pack(fill="x")

        ttk.Label(card, text="First number", style="Field.TLabel").pack(anchor="w")
        self.first_input = ttk.Entry(card, font=("Helvetica", 13))
        self.first_input.pack(fill="x", pady=(8, 18))

        ttk.Label(card, text="Operation", style="Field.TLabel").pack(anchor="w")
        self.operation_input = ttk.Combobox(
            card,
            values=tuple(OPERATIONS),
            state="readonly",
            font=("Helvetica", 12),
        )
        self.operation_input.current(0)
        self.operation_input.pack(fill="x", pady=(8, 18))

        ttk.Label(card, text="Second number", style="Field.TLabel").pack(anchor="w")
        self.second_input = ttk.Entry(card, font=("Helvetica", 13))
        self.second_input.pack(fill="x", pady=(8, 20))

        ttk.Button(
            card,
            text="Calculate",
            style="Calculate.TButton",
            command=self.calculate,
        ).pack(fill="x")

        self.result_label = tk.Label(
            container,
            text="Your result will appear here",
            bg="#EAF0FF",
            fg="#315EFB",
            font=("Helvetica", 14, "bold"),
            padx=16,
            pady=18,
            wraplength=380,
        )
        self.result_label.pack(fill="x", pady=(22, 14))

        ttk.Label(
            container,
            text="Enter two numbers, choose an operation, then calculate.",
            style="Subtitle.TLabel",
        ).pack(anchor="center")

        self.root.bind("<Return>", lambda _event: self.calculate())
        self.first_input.focus_set()

    def calculate(self):
        """Read the two number fields and display the result or an error."""
        try:
            result = calculate_result(
                self.operation_input.get(),
                self.first_input.get().strip(),
                self.second_input.get().strip(),
            )
        except ValueError:
            self.result_label.configure(
                text="Please enter a valid number in both fields.",
                bg="#FFF1F0",
                fg="#B42318",
            )
            return

        is_error = isinstance(result, str)
        self.result_label.configure(
            text=format_result(result),
            bg="#FFF1F0" if is_error else "#EAF0FF",
            fg="#B42318" if is_error else "#315EFB",
        )


def run_app():
    """Create the window and start the Tkinter event loop."""
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_app()
