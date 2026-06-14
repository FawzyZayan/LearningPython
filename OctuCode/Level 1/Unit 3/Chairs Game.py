chair_number = int(input("Enter your Chair Number: "))
if chair_number == 21:
  print("Congratulations you won! The number was 21")
else:
  print(f"Oops you lost! The number was not {chair_number}. Try Again")

print("____________________________________________")

print("***A NEW GAME***")

chair_number_two = int(input("Enter your Chair Number: "))
if chair_number_two != 13:
  print(f"Congratulations you won! The number was {chair_number_two}")
else:
  print("Oops you lost! The number was not 13. Try Again")