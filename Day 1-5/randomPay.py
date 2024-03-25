names_string = "John Jai Pookie"  # Corrected to use a string instead of a list

# Split the string into a list of names
names = names_string.split()

import random

num_items = len(names)

# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
