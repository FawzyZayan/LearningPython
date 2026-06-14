password = "a1b2c3"
user_password = input("Enter the Password: ")

while user_password != password:
  print("Incorrect Password! Try Again")
  user_password = input("Enter the Password: ")

print("Correct Password!")