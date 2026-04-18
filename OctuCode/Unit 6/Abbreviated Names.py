name_list = []

names = input("Enter the First and the Last Name of your Freinds Seperated by a Comma: ").split(", ")

for name in names:
  name_list = name.split(" ")
  print(name_list)

print("Abbreviated Names:")

for name in names:
  name_list = name.split(" ")
  first_letter = name_list[0][0]
  last_letter = name_list[1][0]
  
  print(f"{first_letter}.{last_letter}.")
  