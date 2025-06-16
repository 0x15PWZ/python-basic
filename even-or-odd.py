def is_even(n):
    return n % 2 == 0

num = int(input('Enter a number:'))
if is_even(num):
    print(f"Your number:{num} is even")  # True
else:
    print(f"Your number:{num} is odd") # False
