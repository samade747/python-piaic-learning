# The super() Function
# Create a class Person with a constructor that sets the name. Inherit a class Teacher
#  from it, add a subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# Create object of Teacher class
teacher1 = Teacher("Samad", "Python")
print("Teacher Name:", teacher1.name)

# Object ke attributes ko print kar rahe hain
print("Subject:", teacher1.subject)
print("Name:", teacher1.name)