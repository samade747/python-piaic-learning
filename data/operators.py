# 1. Arithmetic Operators
# Used to perform mathematical operations.

x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.333...
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000


# 2. Comparison Operators
# Used to compare two values. Returns True or False.


x = 10
y = 5

print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False


# 3. Logical Operators
# Used to combine conditional statements.

a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False


# 4. Assignment Operators
# Used to assign values to variables.


# Operator	Description	 Example	Equivalent
# =	Assign value	       x = 5	     x = 5
# +=	Add and assign   	x += 3	     x = x + 3
# -=	Subtract and assign	x -= 3	      x = x - 3
# *=	Multiply and assign	x *= 3	   x = x * 3
# /=	Divide and assign	x /= 3	   x = x / 3
# %=	Modulus and assign	x %= 3	    x = x % 3
# **=	Exponent and assign	x **= 3	    x = x ** 3
# //=	Floor divide and assign	x //= 3	  x = x // 3


x = 5

x += 2   # x = x + 2
print(x) # 7

x *= 3   # x = x * 3
print(x) # 21


# 5. Bitwise Operators
# Operate on binary numbers.


# Operator	Description	Example	Binary Result	Output
# &	AND	5 & 3	0101 & 0011	1
# `	`	OR	`5	3`
# ^	XOR	5 ^ 3	0101 ^ 0011	6
# ~	NOT	~5	~0101	-6
# <<	Left shift	5 << 1	0101 << 1	10
# >>	Right shift	5 >> 1	0101 >> 1	2


x = 5   
y = 3

print(x & y)   # 1
print(x | y)   # 7
print(x ^ y)   # 6
print(~x)      # -6
print(x << 1)  # 10
print(x >> 1)  # 2


# 6. Membership Operators
# Operator	Description	Example	Output
# in	Checks if in sequence	'a' in 'apple'	True
# not in	Checks if not in sequence	'x' not in 'apple'	True


x = "apple"

print("a" in x)   # True
print("x" not in x)  # True

text = "Python is fun"
print("Python" in text)      # True
print("Java" not in text)    # True


# 7. Identity Operators

# Operator	Description	Example	Output
# is	Same object?	x is y	True/False
# is not	Not same object?	x is not y	True/False


x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)    # True (same object)
print(x is z)    # False (different objects)
print(x == z)    # True (same value)


# Practice Task
# Write a program to check if a number is even or odd using operators.


number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


a = "samad"
b = "samad"
c = "samad"

print(a is b)    # True (same object)
print(a is not c)  # False (different objects)  
print(a == c)    # True (same value
