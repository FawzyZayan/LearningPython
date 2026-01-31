import random

print ("Welcome to the Rock, Paper, Scissors game: ")
choice = input("Press ENTER to continue or type (Help) for the rules ").capitalize()

if choice == "Help":
  print("""
    ********RULES********
    1) You choose and the computer chooses
    2) Rock smashes Scissors -> Rock wins
    3) Scissors cut Paper -> Scissors win
    4) Paper covers Rock -> Paper wins
  """)

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
choice2 = input("Enter your choice (rock, paper, scissors): ").capitalize()

if computer_choice == choice2:
  print("It's a tie!")
else: 
  if choice2 == "Rock":
    if computer_choice == "Paper":
      print("You lose! Paper covers Rock")
    elif computer_choice == "Scissors":
      print("You win! Rock smashes Scissors")
  elif choice2 == "Paper":
    if computer_choice == "Rock":
      print("You win! Paper covers Rock")
    elif computer_choice == "Scissors":
      print("You lose! Scissors cut Paper")
  elif choice2 == "Scissors":
    if computer_choice == "Rock":
      print("You lose! Rock smashes Scissors")
    elif computer_choice == "Paper":
      print("You win! Scissors cut Paper")
  else:
    print ("RUN again and ENTER (Rock, Paper, Scissors)")


___________________________________________________________________

import random

print ("Welcome to the Rock, Paper, Scissors game: ")
choice = input("Press ENTER to continue or type (Help) for the rules ").capitalize()

if choice == "Help":
  print("""
    ********RULES********
    1) You choose and the computer chooses
    2) Rock smashes Scissors -> Rock wins
    3) Scissors cut Paper -> Scissors win
    4) Paper covers Rock -> Paper wins
  """)

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
choice2 = input("Enter your choice (rock, paper, scissors): ").capitalize()

if choice2 == "Rock" and computer_choice == "Rock":
   print("It's a tie!")
elif choice2 == "Rock" and computer_choice == "Scissors":
  print("You win! Rock smashes Scissors")
elif choice2 == "Rock" and computer_choice == "Paper":
  print("You lose! Paper covers Rock")
elif choice2 == "Paper" and computer_choice == "Paper":
  print("It's a tie!")
elif choice2 == "Paper" and computer_choice == "Rock":
  print("You win! Paper covers Rock")
elif choice2 == "Paper" and computer_choice == "Scissors":
  print("You lose! Scissors cut Paper")
elif choice2 == "Scissors" and computer_choice == "Scissors":
  print("It's a tie!")
elif choice2 == "Scissors" and computer_choice == "Rock":
  print("You lose! Rock smashes Scissors")
elif choice2 == "Scissors" and computer_choice == "Paper":
  print("You win! Scissors cut Paper")
else:
  print("RUN again and ENTER (Rock, Paper, Scissors)")