def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero."

num1 = int(input('Enter a number 1:'))
num2 = int(input('Enter a number 2:'))

print(divide(num1, num2))

