# Constant value for the speed of light in meters per second (m/s)
C: int = 299792458  # The speed of light in m/s

def main():
    """
    Main function to prompt the user for mass in kilograms,
    calculate energy using Einstein's equation E = m * c^2,
    and print the result.
    """

    # Prompt user to enter mass in kilograms and convert it to a float
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula: E = m * c^2
    # The ** operator raises C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the formula being used
    print("\ne = m * C^2...")

    # Print the mass that the user entered
    print("m = " + str(mass_in_kg) + " kg")

    # Print the constant value of the speed of light
    print("C = " + str(C) + " m/s")

    # Print the calculated energy in joules
    print(str(energy_in_joules) + " joules of energy!")

# The standard boilerplate to run the main function
if __name__ == '__main__':
    main()
