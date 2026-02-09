import random

laptop_random_number = random.randint(1000, 9999)
print(laptop_random_number)

user_password_guessing = int(input("Enter a 4-digit PIN password: "))

if len(str(user_password_guessing)) != 4:
  print("Please enter a 4-digit PIN password")
  
elif user_password_guessing == laptop_random_number:
  print("Success! The PIN password matched")
  
else:
  print("Failure! The PIN password didn't match")
  print(f"The laptop generated this PIN: {laptop_random_number}")