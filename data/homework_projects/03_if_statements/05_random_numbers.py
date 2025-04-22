import random  # Importing the random module so we can generate random numbers

N_NUMBERS: int = 10   # Total numbers we want to generate
MIN_VALUE: int = 1    # The smallest possible random number
MAX_VALUE: int = 100  # The largest possible random number

def main():
    # Create an empty list to store the random numbers
    numbers = []

    # Repeat the loop N_NUMBERS times to generate that many random numbers
    for _ in range(N_NUMBERS):
        # Generate a random number between MIN_VALUE and MAX_VALUE (inclusive)
        num = random.randint(MIN_VALUE, MAX_VALUE)
        numbers.append(num)  # Add the number to our list

    # Print the list of random numbers
    print("Random numbers:", numbers)


# This runs the main function when the script is executed
if __name__ == '__main__':
    main()


# 🧠 What You Learned:
# random.randint(a, b): Generates a random number between a and b (including both).

# List: We use numbers = [] to store our results.

# for _ in range(N_NUMBERS): Runs the loop 10 times (you can use _ when you don’t need the loop variable).

# .append(): Adds each random number to the list.