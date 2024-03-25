import random

def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Ask the user to guess the number
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Run the game
guess_the_number()
