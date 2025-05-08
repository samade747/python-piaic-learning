# Aggregation
# Create a class Department and a class Employee. Use aggregation by having a Department 
# object store a reference to an Employee object that exists independently of it.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  # Employee object reference stored in Department
        # Employee object ko Department ke andar store kiya gaya hai

    def show_info(self):
        print(f"Department: {self.name}")
        print(f"Employee Name: {self.employee.name}")

emp1 = Employee("Samad", 500000, "+923328222026")


dept1 = Department("IT", emp1)  # Employee object passed to Department
dept1.show_info()  # Displaying department and employee information