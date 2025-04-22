PETURKSBOUIPO_AGE: int = 16  # Minimum voting age in Peturksbouipo
STANLAU_AGE: int = 25         # Minimum voting age in Stanlau
MAYENGUA_AGE: int = 48        # Minimum voting age in Mayengua

def main():
    # Ask the user to enter their age (convert it to an integer)
    user_age = int(input("How old are you? "))

    # Check if user is old enough to vote in Peturksbouipo
    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

    # Check if user is old enough to vote in Stanlau
    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    # Check if user is old enough to vote in Mayengua
    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Mayengua where the voting age is " + str(MAYENGUA_AGE) + ".")


# This makes sure the program runs when the file is executed directly
if __name__ == '__main__':
    main()


# 🧠 What You Learned:
# Variables like PETURKSBOUIPO_AGE store age limits.

# input() gets data from the user, and we use int() to convert it from a string to a number.

# if statements let us check conditions, like whether the user is old enough.

# >= means "greater than or equal to."

# str() converts a number into text so we can combine it with strings in print().