"""Number guessing game with hints, attempt count, and multiple rounds."""

import random

def play_round():
    # The computer chooses a secret number from 1 to 100.
    secret_number = random.randint(1, 100)
    attempts = 0
    print("\nI have chosen a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if not 1 <= guess <= 100:
            print("Please enter a number from 1 to 100.")
            continue
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s).")
            break

def main():
    print("===== NUMBER GUESSING GAME =====")
    while True:
        play_round()
        again = input("\nWould you like to play another round? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
