MAX_LENGTH: int = 3  # This sets the maximum allowed length of the list to 3

def shorten(lst):
    # This loop keeps removing the last item from the list until its length is 3 or less
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()  # Remove the last element from the list
        print(last_elem)  # Print the removed element


def get_lst():
    # This function lets the user enter list items one at a time
    # It stops when the user presses Enter without typing anything
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    
    while elem != "":
        lst.append(elem)  # Add each input to the list
        elem = input("Please enter an element of the list or press enter to stop. ")
    
    return lst  # Return the completed list


def main():
    # This is the main function that runs everything
    lst = get_lst()  # Get the full list from the user
    shorten(lst)     # Remove items from the end if list is too long


# This makes sure the program runs only when the file is executed directly
if __name__ == '__main__':
    main()


# 🧠 What You Learned:
# Constants: MAX_LENGTH is a constant that controls how long the list is allowed to be.

# Loop with condition: while len(lst) > MAX_LENGTH keeps running as long as the list is too long.

# .pop(): Removes and returns the last element of the list.

# Modular code: get_lst() and shorten() are two functions with different jobs—this is a clean way to build programs.