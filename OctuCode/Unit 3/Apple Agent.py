area = input("Enter one of these areas: Cairo, Alexandria or Giza: ")

if area.upper() == "CAIRO":
  print("You entered Cairo")
  print("*****Cairo*****")
  print("Your Apple Agent is called Tarek Ahmed")
  print("He is 27 years old")
  print("He is friendly, hardworking and easygoing")
  print("He will be your Apple Agent")
  
elif area.upper() == "ALEXANDRIA":
  print("You entered Alexandria")
  print("*****Alexandria*****")
  print("Your Apple Agent is called Mohammed Yasin")
  print("He is 41 years old")
  print("He is annoyend easily and shy")
  print("He will be your Apple Agent")
  
elif area.upper() == "GIZA":
  print("You entered Giza")
  print("*****Giza*****")
  print("Your Apple Agent is called Ashraf Emam")
  print("He is 36 years old")
  print("He is freindly and cooperating")
  print("He will be your Apple Agent")
  
else:
  print(f"Sorry, {area} is not in our list")
  print("Please follow the instructions")