import random

number = random.randint(1, 10000)

guess = int(input("Enter a number from 1 to 10000: "))

while guess != number:
  if guess > number:
    print("Too High! Try Again")
    guess = int(input("Enter a number from 1 to 10000: "))
  else:
    print("Too Low! Try Again")
    guess = int(input("Enter a number from 1 to 10000: "))
    
print("Congratulations! You Guessed the Number!")