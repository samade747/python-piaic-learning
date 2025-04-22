def get_first_element(lst):
    # This function receives a list called lst and prints its first element (index 0)
    print(lst[0])


def get_lst():
    # This function lets the user keep entering items one by one to build a list
    # It stops when the user presses Enter without typing anything
    lst = []  # Start with an empty list
    elem = input("Please enter an element of the list or press enter to stop. ")
    
    # Keep asking for input until the user presses Enter with no input
    while elem != "":
        lst.append(elem)  # Add the input to the list
        elem = input("Please enter an element of the list or press enter to stop. ")
    
    return lst  # Return the complete list


def main():
    # This is the main function that runs the program
    lst = get_lst()  # Get a list from the user
    get_first_element(lst)  # Print the first item in that list


# This line checks if this file is being run directly (not imported somewhere else)
if __name__ == '__main__':
    main()  # Start the program by calling main()
