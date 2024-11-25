# Guess the Number
# 24.11.2024

import random

print("Welcome to the Guess the Number game!")
print('''
The program will pick a random number between 1 and 100,
and your goal is to guess it. After each guess,
the program will tell you if the number is higher or lower.
Keep guessing until you find the correct number,
and the program will count the number of attempts.
''')

secret_number = random.randint(1, 100)
print("The program has picked a number, the game has started!")

guess = 0
tries = 0
user_input = ""

while guess != secret_number:

    user_input = input("\nEnter a number: ")
    try:
        guess = int(user_input)
    except ValueError:
        print("[Error] You entered an invalid character.")
        continue
    if guess < 1 or guess > 100:
        print("[Error] You entered an invalid number.")
        continue

    tries += 1

    if secret_number > guess:
        print("Higher!")
    elif secret_number < guess:
        print("Lower!")
    else:
        print(f"Correct! You guessed the number in {tries} attempts. Well done!")
        break