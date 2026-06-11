import sys

travel_list = input("Enter the name of the countries seperated by a comma: ").split(", ")

for country in travel_list:
  print(country)
  visited = input(f"have you ever Visited {country} before? (Yes or No): ").capitalize()
  if visited == "Yes":
    print("I hope you had great time there!")
  elif visited == "No":
    print("I hope you visit this country soon")
  else:
    print("Please follow the Rules")
    sys.exit(0)
    
  print("-------")
  
input("Press Enter To Exit...")