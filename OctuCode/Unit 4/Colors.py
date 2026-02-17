colors = []

first_color = input("Enter the first color you like: ")

colors.append(first_color)

yes_or_no = input("Do you want to add more colors? Yes or No: ").lower()

if yes_or_no == "yes":
  second_color = input("Add another color to the list: ")
  colors.append(second_color)
  print("The colors you like are:")
  print(colors)
  
elif yes_or_no == "no":
  print("The color you like is:")
  print(colors)
  
else:
  print("Please follow the instructions")