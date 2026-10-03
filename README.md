# Calculator

A typed, menu-driven calculator for IE Python I (Session 1). It adds, subtracts, multiplies and divides two numbers, refuses division by zero, and never crashes on bad input.

## Project structure

```
calculator/
├── calculator.py            # the four operations + the menu loop
├── tests/
│   └── test_calculator.py   # normal and boundary-case tests
├── data/                    # reserved for future data files
├── pyproject.toml           # project metadata (managed by uv)
├── uv.lock                  # exact dependency versions
├── .python-version          # Python 3.13
└── README.md
```

## Setup

Requires [uv](https://docs.astral.sh/uv/).

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

## Design choices

- **Logic separated from input/output.** The four operations never call `input()` or `print()`; only `main()` talks to the user. That keeps the maths easy to test and reuse.
- **Division by zero raises `ValueError`** instead of returning 0. A silent 0 would look like a real result in a financial report; an error makes the problem visible, and the menu checks for zero first and shows a friendly message.
- **Invalid input never crashes the program.** Typing letters instead of a number shows a message and goes back to the menu.
