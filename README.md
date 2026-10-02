# Calculator

A typed, menu-driven calculator for IE Python I (Session 1). It adds, subtracts, multiplies and divides two numbers, refuses division by zero, and never crashes on bad input.

## Project structure

```
calculator/
├── main.py                  # menu loop: reads input, prints results
├── src/
│   └── calculator.py        # add, subtract, multiply, divide (pure, typed functions)
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
uv run main.py
```

Choose 1 to 4 for an operation, enter two numbers, and 5 to exit.

## Tests

```bash
uv run python -m tests.test_calculator
```

## Design choices

- **Logic separated from input/output.** The operations in `src/calculator.py` never call `input()` or `print()`, so they can be tested directly and reused elsewhere.
- **Division by zero raises `ValueError`** instead of returning 0. A silent 0 would look like a real result in a financial report; an error makes the problem visible, and the menu turns it into a friendly message.
- **Invalid input is retried, not fatal.** Typing letters instead of a number asks again rather than crashing.
