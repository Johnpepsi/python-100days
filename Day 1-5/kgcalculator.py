print("Welcome to KG Calculator " + input("What is your name? ")+ "\n")

height = float(input("Enter your height in meters: ")) # in meters
weight = int(input("Enter your weight in kg: ")) # in kg

bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you're in normal weight")
elif bmi < 30:
    print(f"Something is not right {bmi}, with the result")
elif bmi < 35:
    print(f"You have a {bmi}, and a little bit of obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")