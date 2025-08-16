import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to Guess Number Game")

    while True:

        try:
            guess = int(input("Enter your guess (1 - 100): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"\nCongratulations! You guessed it in {attempts} attempts.")

            break