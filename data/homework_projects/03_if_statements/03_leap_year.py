def main():
    # Ask the user to type a year and convert it to an integer
    year = int(input('Please input a year: '))

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If it is, check if it is also divisible by 100
        if year % 100 == 0:
            # If it is divisible by 100, then it must also be divisible by 400 to be a leap year
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            # If divisible by 4 but not 100, it's a leap year
            print("That's a leap year!")
    else:
        # If not divisible by 4 at all, it's not a leap year
        print("That's not a leap year.")


# This runs the main() function only if the file is executed directly
if __name__ == '__main__':
    main()



# 🧠 What You Learned About Leap Years:
# A year is a leap year if:

# It is divisible by 4

# Except when it's divisible by 100

# Unless it's also divisible by 400

# For example:

# 2000 → ✅ leap year (divisible by 400)

# 1900 → ❌ not a leap year (divisible by 100 but not 400)

# 2024 → ✅ leap year (divisible by 4, not 100)