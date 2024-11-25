# Guess the Number by SOLN4R
# version 1.0: 24.11.2024
# version 1.01: 25.11.2024

import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRIES = 10

def print_rules() -> None:
    print("Welcome to the Guess the Number game!")
    print(f'''
The program will pick a random number between {MIN_NUMBER} and {MAX_NUMBER},
and your goal is to guess it. After each guess,
the program will tell you if the number is higher or lower.
Keep guessing until you find the correct number,
and the program will count the number of attempts.
You have a maximum of {MAX_TRIES} attempts.
    ''')

def get_user_guess() -> int:
    while True:
        user_input = input(f"Enter a number ({MIN_NUMBER}-{MAX_NUMBER}): ")
        try:
            guess = int(user_input)
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
            else:
                print(f"[Error] Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.\n")
        except ValueError:
            print("[Error] You entered an invalid character.\n")

def play_game() -> None:
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print("\nThe program has picked a number, the game has started!\n")
    print(secret_number)
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()
        tries += 1

        if secret_number > guess:
            print("Higher!\n")
        elif secret_number < guess:
            print("Lower!\n")
        else:
            print(f"Correct! You guessed the number in {tries} attempts. Well done!")
            return

    print(f"Game over! You've used all {MAX_TRIES} attempts. The correct number was {secret_number}.")

def main() -> None:
    print_rules()
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()