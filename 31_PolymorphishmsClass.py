class Bird:
    def fly(self):
        print("Bird can fly 🐦")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly ❌")

def test_fly(animal):
    animal.fly()

test_fly(Bird())
test_fly(Penguin())
