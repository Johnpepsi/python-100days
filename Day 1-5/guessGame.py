# Learning: How to use the Random numbers

print("Welcome to the Head and Tails Guessing Game! \n")

import random

guessing_game = random.randint(1, 2)

if guessing_game == 1:
    print("Heads")
else:
    print("Tails")
