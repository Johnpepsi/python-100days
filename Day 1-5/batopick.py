import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_icons = [rock, paper, scissors]

user_choice = int(input("Hey! Enter 0 for Rock | Enter 1 for Paper | Enter 2 for Scissors\nEnter here: "))
print(game_icons[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer choice {computer_choice}")

if user_choice == 0 and computer_choice == 2:
  print("You win Champ!")
  print(scissors)
elif computer_choice > user_choice:
  print("You lose :(")
elif computer_choice == user_choice:
  print("It's a draw!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose, Better luck next time! ")
  print(scissors)
elif computer_choice == 0 and user_choice == 1:
  print("You win Champ!")
  print(rock)
elif user_choice > computer_choice:
  print("You win Champ!")
else:
  print("You type an invalid number, you lose!")