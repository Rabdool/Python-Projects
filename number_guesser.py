import random

def number_guesser():
    print("🎯 Welcome to Number Guesser!")
    lower = 1
    upper = 100
    secret_number = random.randint(lower, upper)
    attempts = 0

    print(f"I'm thinking of a number between {lower} and {upper}. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower or guess > upper:
                print(f"Please guess a number between {lower} and {upper}.")
            elif guess < secret_number:
                print("Too low. Try again.")
            elif guess > secret_number:
                print("Too high. Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    number_guesser()
