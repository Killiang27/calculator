from src.calculator import add, subtract, multiply, divide


def main():
    while True:
        print("\n1) Add  2) Subtract  3) Multiply  4) Divide  5) Exit")
        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye Mate!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid option, choose 1 to 5.")
            continue

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            if b == 0:
                print("Undefined!")
            else:
                print("Result:", divide(a, b))


if __name__ == "__main__":
    main()
