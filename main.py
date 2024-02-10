import random

lower_number = 1
upper_number = 100
max_attempts = 10

secret_number = random.randint(lower_number, upper_number)

def guess_number():
    guess = int(input(f"Guess a number between {lower_number} and {upper_number}: "))
    if lower_number <= guess <= upper_number:
        return guess
    else:
        print("Invalid number input")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = guess_number()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print("You guessed well")
            won = True
            break
        else:
            print("Try again")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()
