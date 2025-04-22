def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)

########## No need to edit code past this point

def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()



# 🔍 Line-by-line Explanation
# 1. def add_three_copies(my_list, data):
# def means we are defining a function.

# add_three_copies is the name of the function.

# my_list and data are parameters (like inputs to the function).

# 2. for i in range(3):
# This is a loop that runs 3 times.

# range(3) creates numbers: 0, 1, 2.

# So the code inside the loop will run 3 times.

# 3. my_list.append(data)
# append() adds data to the end of my_list.

# After 3 loops, the message is added 3 times.

# 4. def main():
# This is another function named main.

# It's where the main program logic happens.

# 5. message = input("Enter a message to copy: ")
# input() asks the user to type something.

# Whatever they type is stored in message.

# 6. my_list = []
# This creates an empty list named my_list.

# 7. print("List before:", my_list)
# Shows the list before adding anything. It'll be [].

# 8. add_three_copies(my_list, message)
# Calls the function to add the message 3 times to the list.

# 9. print("List after:", my_list)
# Shows the list after adding the message 3 times.

# 10. if __name__ == "__main__":
# This means: "Only run the main() function if this file is being run directly (not imported)."

# 11. main()
# Calls the main() function to start the program.

