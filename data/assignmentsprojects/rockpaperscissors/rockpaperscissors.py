# Importing the random module to generate random choices for the computer
import random  

# Function to play the Rock-Paper-Scissors game
def play():  
    # Asking the user to enter their choice: 'r' for rock, 'p' for paper, 's' for scissors
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")  

    # Computer randomly selects one option from 'r', 'p', or 's'
    computer = random.choice(['r', 'p', 's'])  

    # If the user and computer select the same option, the game is a tie
    if user == computer:  
        return "It's a tie"  # Returning the result as a string

    # Checking if the user wins by calling the is_win function
    if is_win(user, computer):  
        return "You won!"  # Returning the result if the user wins

    # If the user doesn't win and it's not a tie, the user loses
    return "You lost!"  

# Function to check if the player wins
def is_win(player, opponent):  
    # Defining the winning conditions:
    # Rock ('r') beats Scissors ('s')
    # Scissors ('s') beats Paper ('p')
    # Paper ('p') beats Rock ('r')
    
    # Checking if the player's choice beats the opponent's choice
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):  
        return True  # If any condition is met, the player wins

# Calling the play function and printing the result to start the game
print(play())  
