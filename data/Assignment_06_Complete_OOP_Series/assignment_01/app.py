#  1. Using self
#  Create a class Student with attributes name and marks. Use the self keyword to
#  initialize these values via a constructor. Add a method display() that prints

#  student details.

#  class
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


Student1 = Student("samad", 99)
Student1.display()


Student2 = Student("mar", 99)
Student1.display()