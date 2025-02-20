

# Guess the Number Game (Player vs Computer & Computer vs Player)
import random  # Importing the random module to generate random numbers

# Function where the user tries to guess the randomly chosen number
def guess(x):
    
    random_number = random.randint(1, x)  # Generates a random number between 1 and x
    guess = 0  # Initializing guess to 0 so that the loop starts
    while guess != random_number:  # The loop runs until the user guesses correctly
        guess = int(input(f"Guess a number between 1 and {x}: "))  # Asking the user for input
        if guess < random_number:  # If guess is less than the number
            print("Sorry, guess again. Too low.")  # Hints that the guess is too low
        elif guess > random_number:  # If guess is greater than the number
            print("Sorry, guess again. Too high.")  # Hints that the guess is too high      
    
    print(f"You have guessed the number {random_number} correctly!")  # Displays success message

# Function where the computer tries to guess the user's chosen number
def computer_guess(x):
    low = 1  # The lower bound of the guessing range
    high = x  # The upper bound of the guessing range
    feedback = ''  # Variable to store user feedback
    
    while feedback != 'c':  # The loop continues until the computer guesses correctly
        if low != high:  # If the range is not reduced to one number
            guess = random.randint(low, high)  # Computer randomly picks a number in the range
        else:
            guess = low  # If low and high are the same, that's the number to guess
        
        # Asking for user feedback: Is the guess too high, too low, or correct?
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == 'h':  # If guess is too high
            high = guess - 1  # Adjust the upper bound to one less than the guessed number
        elif feedback == 'l':  # If guess is too low
            low = guess + 1  # Adjust the lower bound to one more than the guessed number
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!')  # Success message

# Calling the function to start the game where the user guesses the number
guess(10)








# # Guess the Number Game Python Project (computer)
# #guessing game by 
# import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry, guess again. Too low.")
#         elif guess > random_number:
#             print("Sorry, guess again. Too high.")      
            
#     print(f"You have guessed the number {random_number} correctly!")

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low # could also be high b/c low = high
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'Yay! The computer guessed your number, {guess}, correctly!')


# guess(10)

