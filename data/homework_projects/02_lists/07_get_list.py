def main():
    lst = []  # Create an empty list to store user inputs

    val = input("Enter a value: ")  # Ask the user to enter something

    # Keep asking for values until the user just presses Enter (empty input)
    while val:
        lst.append(val)  # Add the user's input to the list
        val = input("Enter a value: ")  # Ask for the next input

    # Show the final list after the loop ends
    print("Here's the list:", lst)


# This runs the main() function only if this script is executed directly
if __name__ == '__main__':
    main()


# 🧠 What You Learned:
# How to create an empty list: lst = []

# How to use a loop to keep asking the user for input

# How to add items to a list using append()

# How to check for empty input to stop the loop

# How to display the final list with print()