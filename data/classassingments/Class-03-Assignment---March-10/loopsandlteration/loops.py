# The for Loop

# Iterate over a list
fruits: list = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Note: Membership Operators in Python in, not in



# Iterate over a string
word: str = "Python"
for letter in word:
    print(letter)



# for Loop with else in Python

#  for loop with else (No break)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")



# for loop with break (Skipping else)
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    if num == 3:
        print("Breaking the loop!")
        break
else:
    print("Loop completed successfully!")  # This will NOT run



# Print numbers from 0 to 4
for i in range(5):
    print(i)


# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)



for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    # Code to be executed 100,000 times
    print(f"Hello, World! Iteration { _ }")

# Controlling Loops

# Break example
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4


# Continue example
for i in range(5):
    if i == 3:
        continue
    print(i)  # Prints 0, 1, 2, 4

# Nested Loops

# Multiplication table
for outer in range(1, 6): # outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print()  # Add a blank line after each row


# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)


# Find factors of a number
num: int = 24
factors = []
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num}: {factors}")