import random
import string
import sys

print("Welcome to the Strong Password Generator!")

password_len = int(input("Enter the total number of characters in the password: "))
letters_len = int(input("Enter the total number of letters in the password: "))
numbers_len = int(input("Enter the total number of numbers in the password: "))
symbols_len = int(input("Enter the total number of symbols in the password: "))

all_len = letters_len + numbers_len + symbols_len

if all_len != password_len:
  print("Invalid input. The sum of letters, numbers and symbols doesn't match the password length")
  sys.exit(2)

else:
  letters = random.choices(string.ascii_letters, k=letters_len)
  numbers = random.choices(string.digits, k=numbers_len)
  symbols = random.choices(string.punctuation, k=symbols_len)
  
  password = letters + numbers + symbols
  
  random.shuffle(password)
  
  final_password = "".join(password)
  
  print(f"Generated Password: {final_password}")