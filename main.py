print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

trueword = name1.count("t") + name2.count("t") + name1.count("r") + name2.count("r") + name1.count("u") + name2.count("u") + name1.count("e") + name2.count("e")

loveword = name1.count("l") + name2.count("l") + name1.count("o") + name2.count("o") + name1.count("v") + name2.count("v") + name1.count("e") + name2.count("e")

resulttext = str(trueword) + str(loveword)
resultint = int(resulttext)

if resultint <= 10 or resultint >= 90:
  print(f"Your score is {resultint}, you go together like coke and mentos.")
elif resultint >= 40 and resultint <=50:
  print(f"Your score is {resultint}, you are alright together.")
else:
  print(f"Your score is {resultint}, you are in much love.")
