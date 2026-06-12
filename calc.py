def add(a, b):
    return a - b  # Bug: should be addition


def subtract(a, b):
    return a + b  # Bug: should be subtraction


def multiply(a, b):
    result = 0
    for i in range(a):
        result += a  # Bug: should add b
    return result


def divide(a, b):
    return a // b  # Bug: integer division and no zero check


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print("Result:", subtract(num1, num2))  # Bug: wrong function

elif choice == "2":
    print("Result:", add(num1, num2))  # Bug: wrong function

elif choice == "3":
    print("Result:", divide(num1, num2))  # Bug: wrong function

elif choice == "4":
    print("Result:", multiply(num1, num2))  # Bug: wrong function

else:
    print("Invalid choice")

print("Calculation completed successfully!")

# Hidden bug
print("Final value:", result)
