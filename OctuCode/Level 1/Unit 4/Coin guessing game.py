import random

print("Welcome to the Coin Guessing Game!")

print("Choose a method to toss the coin:")
print("1. Using random.random()")
print("2. Using random.randint()")
choice = input("Enter your choice (1 or 2)")

if choice == "1":
  random_number = random.random()
  if random_number >= 0.5:
    laptop_result = "Heads"
  else:
    laptop_result = "Tails"

elif choice == "2":
  if random.randint(0,1) == 0:
    laptop_result = "Heads"
  else:
    laptop_result = "Tails"
    
else:
  print("Invalid Choice! Please select either 1 or 2")
  
user_choice = input("Enter your guess (Heads or Tails)")

if user_choice.lower() == laptop_result.lower():
  print("Congratulations, you won!")
else:
  print("Sorry, you lost!")
  
print(f"The laptop's coin toss result was: {laptop_result}")