import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0
    while True:
        # Get user input
        guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
