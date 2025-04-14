INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    # Print the result with an appropriate message
    print(f"{feet} feet is equal to {inches} inches.")  # f-string for formatted output