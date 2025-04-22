def read_phone_numbers():
    # Create an empty dictionary to store names and phone numbers
    phonebook = {}

    while True:
        # Ask the user to enter a name
        name = input("Name: ")

        # If the input is blank, stop asking for more entries
        if name == "":
            break

        # Ask the user to enter the phone number for the name
        number = input("Number: ")

        # Add the name and number to the dictionary
        phonebook[name] = number

    # Return the completed phonebook dictionary
    return phonebook


def print_phonebook(phonebook):
    # Go through each name in the phonebook and print their number
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    # Let the user search for phone numbers by name
    while True:
        # Ask for a name to look up
        name = input("Enter name to lookup: ")

        # If input is blank, stop the loop
        if name == "":
            break

        # If the name is not in the phonebook, tell the user
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            # Otherwise, show the number for that name
            print(phonebook[name])


def main():
    # Step 1: Read names and numbers from the user
    phonebook = read_phone_numbers()

    # Step 2: Print the entire phonebook
    print_phonebook(phonebook)

    # Step 3: Let the user look up phone numbers
    lookup_numbers(phonebook)


# Only run main() if this file is being run directly (not imported)
if __name__ == '__main__':
    main()



# 🧠 What You Learned:
# Dictionaries are used to store key-value pairs like "Alice" : "123456789".

# The while True loops keep asking for input until you break with an empty string.

# You can check if a key exists in a dictionary with if name in phonebook.

# This small project brings together:

# input/output

# loops

# conditionals

# data structures