# student.py

from person import Person

class Student(Person):
    def __init__(self, name, age, height, major):
        # Call the parent class constructor
        super().__init__(name, age, height)
        # Public property
        self.major = major
        print("This time it's a Student object")

# Testing the Student class
if __name__ == "__main__":
    student1 = Student("Maria", 22, 6, "Computer Science")
    print("Student Major:", student1.major)
