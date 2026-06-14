number = 7
user_number = int(input("Enter a number: "))
if user_number != number:
  print(f"Oops you lost! The number was not {user_number}. Try Again")
else:
  print("Congratulations you won! The number was 7")