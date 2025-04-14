

# Import the random module to generate random numbers (used for simulating dice rolls)
import random

# Constant representing the number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice, prints each die value and their total.
    Demonstrates local variable scope.
    """
    # Generate a random number between 1 and NUM_SIDES for the first die
    die1: int = random.randint(1, NUM_SIDES)
    
    # Generate a random number between 1 and NUM_SIDES for the second die
    die2: int = random.randint(1, NUM_SIDES)

    # Calculate the total of both dice
    total: int = die1 + die2

    # Print each die's value and their total
    print(f"Rolled die1: {die1}, die2: {die2} -> Total: {total}")

def main():
    """
    Main function to run the dice simulator.
    Demonstrates how variable 'die1' in this scope is separate from 'die1' inside roll_dice().
    """
    # Define a variable 'die1' in the main function scope and set it to 10
    die1: int = 10

    # Print the initial value of 'die1' in main (not affected by roll_dice)
    print("die1 in main() starts as:", die1)

    # Roll the dice 3 times using a loop
    for i in range(1, 4):
        print(f"\nRolling dice - Attempt {i}")
        roll_dice()  # Call the function to simulate a dice roll

    # Print the final value of 'die1' in main to show it remains unchanged
    print("\ndie1 in main() is still:", die1)

# Standard Python boilerplate: this ensures main() runs when the script is executed directly
if __name__ == '__main__':
    main()
