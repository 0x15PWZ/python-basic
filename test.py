import my_tools
from my_tools import subtract as s
from my_tools import multiply as m
from my_tools import divide as d
from my_tools import power as p


num1 = int(input('Enter a number 1: '))
num2 = int(input('Enter a number 2: '))

print(f"{num1} + {num2} = {my_tools.add(num1, num2)}")  # Adding
print(f"{num1} - {num2} = {s(num1, num2)}")  # Subtraction
print(f"{num1} * {num2} = {m(num1, num2)}")  # Multiplication
print(f"{num1} / {num2} = {d(num1, num2)}")  # Division
print(f"{num1} ** {num2} = {p(num1, num2)}")  # Power
