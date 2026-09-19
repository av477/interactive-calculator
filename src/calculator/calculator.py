"""Here is the Core calculator logic for the interactive calculator project."""

from __future__ import annotations

from colorama import Fore, Style, init

init(autoreset=True)


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate(a: float, operation: str, b: float) -> float:
    """Perform a calculation on two numbers based on a user-selected operation."""
    op = operation.strip().lower()
    operations = {
        "+": add,
        "add": add,
        "sum": add,
        "-": subtract,
        "subtract": subtract,
        "minus": subtract,
        "*": multiply,
        "multiply": multiply,
        "times": multiply,
        "/": divide,
        "divide": divide,
        "div": divide,
    }

    if op not in operations:
        raise ValueError(
            "Invalid operation. Choose one of: add, subtract, multiply, divide."
        )

    return operations[op](a, b)


def evaluate_expression(expression: str) -> float:
    """Evaluate a arithmetic expression using Python's evaluator."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
    except Exception as exc:  # catch any exception and raise a ValueError with a helpful message
        raise ValueError(f"Invalid expression: {expression}") from exc

    if isinstance(result, (int, float)):
        return float(result)

    raise ValueError(f"Expression did not produce a number: {expression}")


def _parse_number(raw_value: str, label: str) -> float:
    """Convert a user-entered number string into a float or raise a helpful error."""
    try:
        return float(raw_value)
    except ValueError as exc:
        raise ValueError(f"Invalid {label} number: {raw_value!r}. Please enter a valid number.") from exc


def run_interactive() -> None:
    """Run a simple interactive calculator loop in the terminal."""
    print("-------------------- Interactive Calculator --------------------")
    print("Available operations: add, subtract, multiply, divide")
    print("----------------------------------------------------------------")
    print(Fore.YELLOW + "For addition, enter: add, sum, or +")
    print(Fore.YELLOW + "For subtraction, enter: subtract, minus, or -")
    print(Fore.YELLOW + "For multiplication, enter: multiply, times, or *")
    print(Fore.YELLOW + "For division, enter: divide, div, or /")
    print("----------------------------------------------------------------")
    print("Type 'quit' or 'exit' to exit the calculator.")

    while True:
        operation = input("Choose an operation: ").strip()

        if operation.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        try:
            if operation.lower() not in {
                "+",
                "-",
                "*",
                "/",
                "add",
                "subtract",
                "multiply",
                "divide",
                "sum",
                "minus",
                "times",
                "div",
            }:
                raise ValueError(
                    "Invalid operation. Choose one of: add or +, subtract or -, multiply or *, divide or /."
                )

            first_number = _parse_number(input("Enter the first number: ").strip(), "first")
            second_number = _parse_number(input("Enter the second number: ").strip(), "second")
            result = calculate(first_number, operation, second_number)
            print(f"Result: {result}")
        except ValueError as exc:
            print(f"Error: {exc}")
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    run_interactive()
