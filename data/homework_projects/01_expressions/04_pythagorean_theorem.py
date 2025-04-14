# Import the math module to use the square root function
import math

def main():
    """
    This function calculates the hypotenuse of a right triangle
    using the Pythagorean theorem: hypotenuse² = side1² + side2²
    """

    # Get the length of side AB from the user and convert it to a float
    ab: float = float(input("Enter the length of AB: "))

    # Get the length of side AC from the user and convert it to a float
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse (BC) using math.sqrt
    bc: float = math.sqrt(ab**2 + ac**2)

    # Print the result
    print("The length of BC (the hypotenuse) is: " + str(bc