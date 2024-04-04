import random
import itertools

# lists
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0','1','2','3','4','5','6','7','8','9']
syms = ['!','@','#','$','%','^','&','*','+','_']

# inputs
print("Python Password Generator : \n")
charAmount = int(input("How many letters would you like to have in your password? : "))
numAmount = int(input("How many numbers? : "))
symAmount = int(input("How many symbols? : "))

# random num/sym/char

randomNum = ""
for num in nums :
  if int(num) < numAmount :
    randomNum += nums[random.randint(0,9)]


randomSym = ""
for sym in range(0, symAmount):
  if sym < symAmount :
    randomSym += syms[random.randint(0,9)]


randomChar = ""
for char in range(0, charAmount) :
  if sym < charAmount :
    randomChar += chars[random.randint(0, 25)]


# Final Password generator
generatorList = list(itertools.chain(randomNum,randomSym,randomChar))

Password = ""
tot = len(generatorList)
for word in generatorList:
      Password += generatorList[random.randint(0,tot)]

print(f"Your new password is : {Password}")
