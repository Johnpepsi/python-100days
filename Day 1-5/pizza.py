print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")

# Initialize bill and extra variables
bill = 0
extra = 0

# lower() method is used to convert the input to lowercase for case-insensitive comparison
if size.lower() == "s":
    bill += 6
    print("Small pizza is $6.")
elif size.lower() == "m":
    bill += 8
    print("Medium pizza is $8.")
elif size.lower() == "l":
    bill += 10
    print("Large pizza is $10.")
else:
    print("Invalid input.")

# Check if the customer wants pepperoni
wants_add_pepperoni = input("Do you want pepperoni? Y or N: ")
if wants_add_pepperoni.lower() == "y":
    bill += 2
    print("Pepperoni added for $2.")
elif wants_add_pepperoni.lower() == "n":
    print("No problem!")

# Check if the customer wants extra cheese
wants_extra_cheese = input("Do you want extra cheese? Y or N: ")
if wants_extra_cheese.lower() == "y":
    extra += 1.22
    print("Extra cheese added for $1.22.")
elif wants_extra_cheese.lower() == "n":
    print("No problem!")

# Calculate and print the final bill
final_bill = bill + extra
print(f"Your final bill is: ${final_bill}.")
