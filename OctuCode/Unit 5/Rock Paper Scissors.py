import random

choices = [ "Rock", "Paper", "Scissors" ]

print("Welcome to Rock Paper Scissors Game!")

help_or_skip = input("Press Enter to Play or Type 'Help' to See the Rules: ").capitalize()

if help_or_skip == "Help":
  
  print("""
        ********* RULES *********
        1) You will Choose and the Computer will Choose
        2) Rock Beats Scissors
        3) Scissors Beats Paper
        4) Paper Beats Rock
        """)
  
  computer_choice = random.choice(choices)
  
  your_choice = input("Please Choose Rock Paper Scissors: ").capitalize()
  
  if computer_choice == "Rock" and your_choice == "Rock":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("It's A Tie!")
    
  elif computer_choice == "Paper" and your_choice == "Paper":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("It's A Tie!")
    
  elif computer_choice == "Scissors" and your_choice == "Scissors":
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          """)
    
    print("It's A Tie!")
    
  elif computer_choice == "Rock" and your_choice == "Paper":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("You Won! Paper Beats Rock!")
    
  elif computer_choice == "Rock" and your_choice == "Scissors":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("You Lose! Rock Beats Scissors!")
    
  elif computer_choice == "Paper" and your_choice == "Rock":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("You Lose! Paper Beats Rock!")
    
  elif computer_choice == "Paper" and your_choice == "Scissors":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("You Won! Scissors Beats Paper!")
    
  elif computer_choice == "Scissors" and your_choice == "Rock":
        
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("You Won! Rock Beats Scissors!")
    
  elif computer_choice == "Scissors" and your_choice == "Paper":
        
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("You Lose! Scissors Beats Paper!")
    
  else:
        
    print("Please Run the Program Again and Press Enter to Play or Type 'Help' to See the Rules")

elif help_or_skip != "Help" and help_or_skip != "":
  
  print("Please Run the Program Again and Press Enter to Play or Type 'Help' to See the Rules")
  
else:
  
  computer_choice = random.choice(choices)
  
  your_choice = input("Please Choose Rock Paper Scissors: ").capitalize()
  
  if computer_choice == "Rock" and your_choice == "Rock":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("It's A Tie!")
    
  elif computer_choice == "Paper" and your_choice == "Paper":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("It's A Tie!")
    
  elif computer_choice == "Scissors" and your_choice == "Scissors":
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

          """)
    
    print("It's A Tie!")
    
  elif computer_choice == "Rock" and your_choice == "Paper":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("You Won! Paper Beats Rock!")
    
  elif computer_choice == "Rock" and your_choice == "Scissors":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("You Lose! Rock Beats Scissors!")
    
  elif computer_choice == "Paper" and your_choice == "Rock":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("You Lose! Paper Beats Rock!")
    
  elif computer_choice == "Paper" and your_choice == "Scissors":
    
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("You Won! Scissors Beats Paper!")
    
  elif computer_choice == "Scissors" and your_choice == "Rock":
        
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
          """)
    
    print("You Won! Rock Beats Scissors!")
    
  elif computer_choice == "Scissors" and your_choice == "Paper":
        
    print("Computer Choice:")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          """)
    
    print("your Choice:")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
          """)
    
    print("You Lose! Scissors Beats Paper!")
    
  else:
        
    print("Please Run the Program Again and Press Enter to Play or Type 'Help' to See the Rules")