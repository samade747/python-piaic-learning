# class methods = allow operations related to the classs itself
    # take (clcss) as the first parameter whici represnts the class it

class Student:

    count = 0
    total_gpa = 0


    def __init__(self, name, gpa):
      self.name = name
      self.gpa = gpa
      Student.count += 1
      Student.total_gpa += gpa

   #instance method
    def get_info(self):
        return f"{self.name} has a {self.gpa} GPA "


    @classmethod
    def get_count(cls):
      return f"there are {cls.count} students"

    @classmethod
    def get_average_gpa(cls):
      if cls.count == 0:
        return 0
      else:
        return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

student1 = Student("samad", 9.7)
student2 = Student("mary", 9.8)
student3 = Student("john", 9.9)

print(Student.get_count())
print(Student.get_average_gpa())


