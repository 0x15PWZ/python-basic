# Class definition
class Student:
    def __init__(self, name, grade):
        self.name = name        # attribute
        self.grade = grade      # attribute

    def show_info(self):        # method
        print(f"👤 Student: {self.name} | 📚 Grade: {self.grade}")


# Object creation
student1 = Student("Aye Aye", "Grade 11")
student2 = Student("Ko Ko", "Grade 10")

# Method call
student1.show_info()
student2.show_info()
