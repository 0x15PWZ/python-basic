text = """DevOps 
with Python"""
name = input('Enter your name:')
age = int(input('Enter your age:'))

print(text.upper())        # DEVOPS WITH PYTHON
print(text.lower())        # devops with python
print(text.strip())        # remove leading/trailing spaces
print(text.replace("Python", "Java"))  # DevOps with Java
print(text.find("Py"))    # index 12
print(text.split())        # ['DevOps', 'with', 'Python']
print(text.replace("Python", "Linux"))
print(text[0])     # D
print(text[-1])    # n
print(text[0:5])   # DevOp
print(text[6:])    # with Python

print(text.count("o"))  # count 1
print(text[::-1]) # reverse string
print("Python" in text)  # Check Python in or not in
print("Java" not in text)  # Check Java in or not in

# Concatenation
print("Name: " + name + ", Age: " + str(age))
# f-string (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")