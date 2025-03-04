#Identity Operators

a = [1, 2, 3]
b = a  # b refers to the same list as a
c = [1, 2, 3]  # c is a different list with the same content

print(a is b)   # True (same memory location)
print(a is c)   # False (different memory locations)
print(a is not c)  # True (not the same memory location)