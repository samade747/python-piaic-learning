# class variables = variables that are shared among all instances of a class
                    #define outside of any methods in the class
                    #allow you to share data amond all objects created from that class

class Student:
    # class variable

    class_year = 2025
    num_studets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_studets += 1

    student1 = Student("samad", 28) # type: ignore
    student2 = Student("mary", 22) # type: ignore