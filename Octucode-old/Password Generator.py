import random
import string

print ("Welcome to the Password Generator!")

length = int (input ("Enter the total number of characters in the password: "))
num_letters = int (input("Enter the number of letters in the password: "))
num_numbers = int (input("Enter the number of numbers in the password: "))
num_symbols = int (input("Enter the number of symbols in the password :"))


if length != (num_letters + num_numbers + num_symbols):
   print ("Invaled input. The sum of letters, numbers, and symbols doesn't match the password length.")
else:
     letters = string.ascii_letters
     numbers = string.digits
     symbols = string.punctuation

     password_char = (
         random.choices(letters, k=num_letters) +
         random.choices(numbers, k=num_numbers) +
         random.choices(symbols, k=num_symbols)
     )

     random.shuffle(password_char)

     password = "".join(password_char)

     print ("Generated Password:", password)