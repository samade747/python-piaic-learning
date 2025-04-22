MINIMUM_HEIGHT: int = 50  # This sets the minimum height required to go on the ride

def main():
    # Ask the user to enter their height, and convert it to a float (decimal number)
    height = float(input("How tall are you? "))

    # Check if the user's height is equal to or greater than the required minimum
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


# This runs the main() function only if the file is executed directly
if __name__ == '__main__':
    main()


# 🧠 What You Learned:
# Constants: MINIMUM_HEIGHT is used to store the minimum height requirement.

# float(input(...)): Converts user input into a decimal number.

# if...else: Makes a decision based on whether the user's height meets the requirement.

# Comparison: >= checks if height is greater than or equal to the minimum.