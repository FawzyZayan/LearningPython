age = int(input("Enter your age: "))
driving_license = input("Do you have a driving license: ")
if age >= 18 and driving_license.upper() == "YES":
  print("You can drive")
elif age < 18 or driving_license.lower() == "no":
  print("You can't drive")
else:
  print("Please follow the instructions")