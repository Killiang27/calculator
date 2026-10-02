"""Menu-driven calculator (command line).

Run with:  uv run main.py
"""

from src.calculator import add, divide, multiply, subtract

MENU = """
=== Calculator ===
1) Add
2) Subtract
3) Multiply
4) Divide
5) Exit"""


def ask_number(prompt: str) -> float:
    """Keep asking until the user types a valid number, then return it."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' is not a number. Please try again.")


def main() -> None:
    """Show the menu, run the chosen operation, repeat until the user exits."""
    while True:
        print(MENU)
        operation = input("Choose an option (1-5): ").strip()

        if operation == "5":
            print("Goodbye!")
            break

        if operation not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose a number from 1 to 5.")
            continue

        a = ask_number("First number: ")
        b = ask_number("Second number: ")

        if operation == "1":
            result = add(a, b)
            symbol = "+"
        elif operation == "2":
            result = subtract(a, b)
            symbol = "-"
        elif operation == "3":
            result = multiply(a, b)
            symbol = "*"
        else:  # operation == "4"
            try:
                result = divide(a, b)
            except ValueError as err:
                print(f"Error: {err}")
                continue
            symbol = "/"

        print(f"Result: {a:g} {symbol} {b:g} = {result:g}")


if __name__ == "__main__":
    main()
