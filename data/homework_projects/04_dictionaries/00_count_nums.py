def get_user_numbers():
    # Create an empty list to store the numbers
    user_numbers = []

    while True:
        # Ask the user to enter a number
        user_input = input("Enter a number: ")

        # If the user presses Enter without typing anything, stop the loop
        if user_input == "":
            break

        # Convert the input into an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)

    # Return the list of numbers the user entered
    return user_numbers

def count_nums(num_lst):
    # Create an empty dictionary to count how many times each number appears
    num_dict = {}

    for num in num_lst:
        # If the number is not yet in the dictionary, add it with count 1
        if num not in num_dict:
            num_dict[num] = 1
        else:
            # If the number is already in the dictionary, increase its count by 1
            num_dict[num] += 1

    # Return the dictionary with counts
    return num_dict

def print_counts(num_dict):
    # Go through each number and its count in the dictionary and print it
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():
    # First, get a list of numbers from the user
    user_numbers = get_user_numbers()

    # Then, count how often each number appears
    num_dict = count_nums(user_numbers)

    # Finally, print the counts
    print_counts(num_dict)

# Run the main function if this file is executed directly
if __name__ == '__main__':
    main()



# 🧠 What You Learned:
# Lists: Used to store the numbers the user enters.

# Dictionaries: Used to keep track of how many times each number appears.

# Loops:

# while True: Keep asking until the user stops.

# for num in num_lst: Go through each number to count them.

# Conditionals: Check if a number is already counted or not.

# Input/Output: Taking input from users and showing results nicely.