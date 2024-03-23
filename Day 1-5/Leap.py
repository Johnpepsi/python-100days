# Learning: How to use if else in Python
# Which year do you want to check?

print("Welcome to the Leap Year Checker! \n")
year = int(input("Enter a Year: "))

if year % 4 == 0:
  if year % 100 == 0:
    # Not a leap year, unless special case
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not Leap year")
  else:
    print("Leap Year")
else:
    print("Not a leap year!")

    # this is a good practice of programming, whenever you get stuck on your logic
    # try to make a flowchart of your logic and then try to implement it in your code
