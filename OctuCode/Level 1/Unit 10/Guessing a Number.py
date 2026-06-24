import random
import os

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")

random_number = random.randint(1, 10)

while True:
  clear_screen()
  user_input = int(input("Guess a number between 1 and 10: "))
  if user_input == random_number:
    print("Congratulations! You guessed the correct number.")
    break
  else:
    print("Wrong guess. Try again")
    input("Press any key to continue...")