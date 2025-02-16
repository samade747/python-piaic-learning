# Assigning a string to a variable
name = "Alice"

# Assigning an integer
age = 25

# Assigning a floating-point number
height = 5.6

# Assigning a boolean
is_student = True

print(name)       # Output: Alice
print(age)        # Output: 25
print(height)     # Output: 5.6
print(is_student) # Output: True


# Original assignment
number = 10
print(number)  # Output: 10

# Reassigning the variable
number = 20
print(number)  # Output: 20


a = b = c = 10
print(a, b, c)  # Output: 10 10 10

x, y, z = 1, 2, 3
print(x, y, z)  # Output: 1 2 3


# Valid variable names
my_variable = "Valid"
_variable = "Also valid"
variable123 = "Valid too"

# Invalid variable names
# 2variable = "Invalid"     # Error
# my-variable = "Invalid"   # Error
# my variable = "Invalid"   # Error


# Saving variables to a file
name = "Alice"
age = 25

with open("data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}")

# Loading variables from a file
with open("data.txt", "r") as file:
    data = file.readlines()
    name = data[0].strip().split(": ")[1]
    age = int(data[1].strip().split(": ")[1])

print(name)  # Output: Alice
print(age)   # Output: 25

# Reading variables from a file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# Dictionary to store variables
person = {
    "name": "Alice",
    "age": 25,
    "height": 5.6
}

# Accessing variables
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 25

# Assigning variables
name = "John"
age = 30
city = "New York"

# Printing the variables
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
