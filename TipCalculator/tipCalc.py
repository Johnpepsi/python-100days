print("Welcome to the tip Calculator")
#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = float(input("What was the total bill? $"))
# print (type(bill))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15: "))
#Format the result to 2 decimal places = 33.60
people = int(input("How many people to split the bill? "))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
each_person_bill = tip / 100 * bill + bill
#Write your code below this line 👇
print(each_person_bill)