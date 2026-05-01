# MY FIRST SIMPLE CALCULATOR
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Enter first number "
    return x / y

print("  Simple Calulator")
print("  oprators: +, -, *, /")

while True:
    num1 = float(input(" Enter first number: "))
    operator = input("What you need to do (+, -, *, /) : ")
    num2 = float(input(" Enter second number : "))

    if operator == '+':
        result = add(num1, num2)
        print("Result:", result)
    elif operator == '-':
        result = subtract(num1, num2)
        print("Result:", result)
    elif operator == '*':
        result = multiply(num1, num2)
        print("Result:", result)
    elif operator == '/':
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print(" Error: This operation is not possible. +, -, *, /")
