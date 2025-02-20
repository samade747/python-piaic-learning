# Guess the Number Game Python Project (user)

import random

class GuessTheNumber:
    def __init__(self, attempts_per_player= 5, min_num= 1, max_num=100):
        self.min_num = min_num
        self.max_num = max_num
        self.attempts_per_player = attempts_per_player
        self.total_attempts = attempts_per_player * 2
        self.secret_number = None

    def set_secret_number(self):
        # admin set the secret number 
        while True:
            try:
                secret = int(input(f"Enter the secret number between {self.min_num} and {self.max_num}: "))
                if self.min_num <= secret <= self.max_num:
                    self.secret_number = secret
                    print("\n" *50)
                    print("Secreat number set! now user 1 and user start guessing. \n")
                    break
                else:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}. try again")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


    def play(self):
        # user 1 & user 2 take turns guessing 
        print(f"User 1 and User 2 have {self.attempts_per_player} attempts each.")

        for attempt in range(1, self.total_attempts + 1):
           player = "User 1" if attempt % 2 != 0 else "User 2"

           try:
                guess = int(input(f"Attempt {attempt}/{self.total_attempts} - {player}, enter your guess: "))

                if guess < self.min_num or guess > self.max_num:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}.")
                    continue

                if guess < self.secret_number:
                    print(f"{player}, Too low! Try again.")
                elif guess > self.secret_number:
                    print(f"{player}, Too high! Try again.")
                else:
                    print(f"🎉 Congratulations {player}! You guessed the number in {attempt} attempts.")
                    return
                
           except ValueError:
                print("Invalid input! Please enter a valid number.")

        print(f"😢 Game over! No one guessed the number. The correct number was {self.secret_number}.")


if __name__ == "__main__":
    game = GuessTheNumberGame() # type: ignore
    game.set_secret_number()  # Admin sets the number
    game.play()  # User 1 and User 2 guess
