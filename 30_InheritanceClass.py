class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):  # Inheriting from Animal
    def speak(self):
        print("Dog barks 🐶")

class Cat(Animal):
    def speak(self):
        print("Cat meows 🐱")


dog = Dog()
dog.speak()

cat = Cat()
cat.speak()
