def input_age(age):
    if age <= 0:
        raise ValueError("Age cannot be zero and negative.")
    return f"Your age is {age}."

count = 0
while True:
    a = int(input('Enter your age: '))
    try:
        print(input_age(a))
        break
    except ValueError as e:
        print("Error:", e)
    count += 1