import random

toohigh = "Too High"
toolow = "Too Low"
print("Welcome to the number guessing gane!\n")
print("I\'m thinking of an integer between 1 and 100:\n")
randominteger = random.randint(1,100)
humanguess = 0
numchanceseasy = 10
numchanceshard = 5
difficulty = input("Choose a difficulty level: Easy or Hard\n")
Ifwon = False
if difficulty == "Easy":
  for i in range(numchanceseasy):
    humanguess = int(input(f"You have {numchanceseasy} attempts remaining to guess the number. Guess one \n"))
    if humanguess == randominteger:
      Ifwon = True
      print("Great! You won!")
      break
    elif humanguess < randominteger:
      Ifwon = False
      print("Too Low")
    elif humanguess > randominteger:
      Ifwon = False
      print("Too High")
    numchanceseasy = numchanceseasy-1
elif difficulty == "Hard":
  for i in range(numchanceshard):
    humanguess = int(input(f"You have {numchanceseasy} attempts remaining to guess the number. Guess one \n"))
    if humanguess == randominteger:
      Ifwon = True
      print("Great! You won!")
      break
    elif humanguess < randominteger:
      Ifwon = False
      print("Too Low")
    elif humanguess > randominteger:
      Ifwon = False
      print("Too High")
    numchanceseasy = numchanceseasy-1#
