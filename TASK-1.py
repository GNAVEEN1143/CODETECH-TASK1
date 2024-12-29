# Basic Calculator 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Take inputs from the usere
operation = input("Enter operation (1/2/3/4): ")

# Perform the operation based on user inputs
if operation == '1':
    print(f"The result is: {add(num1, num2)}")
elif operation == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif operation == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif operation == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input! Please choose a valid operation.")