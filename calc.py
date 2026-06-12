def add(a, b):
    """Returns the sum of two numbers"""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers"""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers"""
    return a * b


def divide(a, b):
    """Returns the quotient of two numbers"""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice: ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

    print("Calculation completed.")


if __name__ == "__main__":
    main()