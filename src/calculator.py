"""Example module demonstrating type checking with basedpyright."""

from typing import Union


def add(a: int, b: int) -> int:
    """Add two integers together.

    Args:
        a: First integer
        b: Second integer

    Returns:
        Sum of a and b
    """
    return a + b


def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of division

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def safe_divide(a: float, b: float) -> Union[float, None]:
    """Safely divide two numbers, returning None on error.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of division or None if b is zero
    """
    try:
        return divide(a, b)
    except ZeroDivisionError:
        return None


class Calculator:
    """A simple calculator class demonstrating instance methods and attributes."""

    def __init__(self, name: str) -> None:
        """Initialize calculator with a name.

        Args:
            name: Name for this calculator instance
        """
        self.name = name
        self.history: list[tuple[str, float]] = []

    def calculate(self, operation: str, a: float, b: float) -> float:
        """Perform a calculation and store in history.

        Args:
            operation: Operation to perform ("+", "-", "*", "/")
            a: First operand
            b: Second operand

        Returns:
            Result of the calculation

        Raises:
            ValueError: If operation is not supported
        """
        result: float

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = divide(a, b)
        else:
            raise ValueError(f"Unsupported operation: {operation}")

        self.history.append((f"{a} {operation} {b}", result))
        return result

    def get_history(self) -> list[tuple[str, float]]:
        """Get calculation history.

        Returns:
            List of (expression, result) tuples
        """
        return self.history.copy()


if __name__ == "__main__":
    # Example usage
    calc = Calculator("MyCalc")

    print(f"10 + 5 = {calc.calculate('+', 10, 5)}")
    print(f"10 - 5 = {calc.calculate('-', 10, 5)}")
    print(f"10 * 5 = {calc.calculate('*', 10, 5)}")
    print(f"10 / 5 = {calc.calculate('/', 10, 5)}")

    print("\nHistory:")
    for expr, result in calc.get_history():
        print(f"  {expr} = {result}")
