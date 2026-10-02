"""Typed multifunction calculator: the four core operations.

Each function is pure: it takes two numbers and returns a result.
No input() or print() here, so every function is easy to test and reuse.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b.

    Args:
        a: First number.
        b: Second number.

    Returns:
        a + b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b.

    Args:
        a: Number to subtract from.
        b: Number to subtract.

    Returns:
        a - b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b.

    Args:
        a: First number.
        b: Second number.

    Returns:
        a * b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Args:
        a: Dividend.
        b: Divisor; must not be zero.

    Returns:
        a / b as a float.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
