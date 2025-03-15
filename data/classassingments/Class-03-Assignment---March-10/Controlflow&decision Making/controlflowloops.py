# Comparison Operators

x: int = 10
y: int = 20

print("x == y = ", x == y)  # False
print("x != y = ", x != y)  # True
print("x > y  = ", x > y)   # False
print("x < y  = ", x < y)   # True
print("x >= y = ", x >= y)  # False
print("x <= y = ", x <= y)  # True


# Logical Operators


age: int = 25
is_student: bool = True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")


# The if Statement

    num: int = 10

if num > 0:
    print("The number is positive.")


# The else Statement


num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")

# The elif Statement

num: int = 0

if num > 0: # Program execution step# 1 if condition = False
    print("The number is positive.")
elif num < 0: # Program execution step# 2 if condition = False
    print("The number is negative.")
else: # Program execution step# 3 python will execute the else block
    print("The number is zero.")

# Nested if Statements

num: int = 10
#num: int = -10

if num > 0: # check wather the number is positive or negative

    if num % 2 == 0: # Modulus operator, remainder 0 = even_number,
        print("The number is positive and even.")
    else: # remainder 1 = odd_number,
        print("The number is positive and odd.")

else:
    print("The number is negative.")

# Practical Examples

operation: str = input("Enter the operation (+, -, *, /): ")
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero."
else:
    result = "Invalid operation."

print("Result:", result)


# building a calculator 


def calculator():
  """
  A calculator function that takes user input for numbers and operations,
  including modulus, floor division, and exponentiation.
  """
  while True:
    operation = input("Enter the operation (+, -, *, /, %, //, ** or 'q' to quit): ")
    if operation.lower() == 'q':
      break
    if operation not in ('+', '-', '*', '/', '%', '//', '**'):
      print("Invalid operation.")
      continue

    try:
      num1 = float(input("Enter the first number: "))
      num2 = float(input("Enter the second number: "))
    except ValueError:
      print("Invalid input. Please enter numbers only.")
      continue

    if operation == '+':
      result = num1 + num2
    elif operation == '-':
      result = num1 - num2
    elif operation == '*':
      result = num1 * num2
    elif operation == '/':
      if num2 != 0:
        result = num1 / num2
      else:
        result = "Error: Division by zero."
        print(result)
        continue
    elif operation == '%':
      result = num1 % num2
    elif operation == '//':
      if num2 != 0:
        result = num1 // num2
      else:
        result = "Error: Division by zero."
        print(result)
        continue
    elif operation == '**':
      result = num1 ** num2

    print("Result:", result)

calculator()

# schoolgrading
def grading_system(marks):
  """
  This function takes marks as input and returns the corresponding grade.

  Args:
    marks: The marks obtained by the student.

  Returns:
    The grade corresponding to the marks.
  """
  if marks >= 90:
    grade = "A+"
  elif marks >= 80:
    grade = "A"
  elif marks >= 70:
    grade = "B"
  elif marks >= 60:
    grade = "C"
  elif marks >= 50:
    grade = "D"
  else:
    grade = "F"
  return grade

# Get marks as input from the user
while True:
  try:
    marks = float(input("Enter the marks: "))
    if 0 <= marks <= 100:
      break
    else:
      print("Marks must be between 0 and 100.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Determine the grade
grade = grading_system(marks)

# Print the grade
print(f"The grade for {marks} marks is: {grade}")
