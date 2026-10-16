# Calculator
Menu style calculator for Python I. It adds, subtracts, multiplies and divides two numbers. It will refuse division by 0 with an error statement, and it won't crash on bad input, just put an error statement and reset.

## Project itself
```
calculator/
-> calculator.py                # the 4 operations and the menu loop
-> tests/ -> test_calculator.py # normal and boundary-case tests
-> data/                        # reserved for future data files
-> pyproject.toml               # project metadata (uv)
-> uv.lock                      # dependencies
-> .python-version              # self explanatory
-> README.md
```

## Setup
```bash
uv sync
```
## Run
```bash
uv run calculator.py
```
Choose 1 to 4 for an operation, enter two numbers, and 5 to exit.
## Tests
```bash
uv run python -m tests.test_calculator
```

## Design choices as gone through in class
Division by zero raises `ValueError` -> instead of returning 0. A silent 0 would look like a real result in a financial report; an error makes the problem visible, and the menu checks for zero first and shows a custom message that I think is friendly.
Invalid input never crashes the program -> Typing letters instead of a number will just show an error message and  will go back to the menu.