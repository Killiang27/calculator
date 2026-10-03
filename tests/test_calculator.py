"""Tests for calculator.py.

Run with:  uv run python -m tests.test_calculator
(or, if pytest is installed:  uv run pytest)
"""

import math

from calculator import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert math.isclose(add(0.1, 0.2), 0.3)


def test_subtract() -> None:
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0
    assert subtract(3, 5) == -2


def test_multiply() -> None:
    assert multiply(3, 4) == 12
    assert multiply(0, 99) == 0
    assert multiply(-2, 3) == -6


def test_divide() -> None:
    assert divide(10, 4) == 2.5
    assert divide(-9, 3) == -3


def test_divide_by_zero_raises() -> None:
    try:
        divide(5, 0)
    except ValueError:
        pass
    else:
        raise AssertionError("divide(5, 0) should raise ValueError")


if __name__ == "__main__":
    tests = [test_add, test_subtract, test_multiply, test_divide, test_divide_by_zero_raises]
    for test in tests:
        test()
        print(f"PASS  {test.__name__}")
    print(f"\nAll {len(tests)} tests passed.")
