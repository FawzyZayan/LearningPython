area = input ("Choose an area: (Cairo), (Kafr EL_Deeb), or (Alexandria) \n")
if area.lower() == "cairo" or area.lower() == "alexandria" or area.lower() == "kafr el_deeb":
  print (f"{area} is on our list!")
else:
  print (f"Sorry, {area} is not on our list!")


#########################################

name = input("Please enter your name:")
password = input("Please enter your password:")
if name.lower() == "fawzy" and password == "123456":
  print ("Welcome back!")
else:
  print ("Sorry, wrong name or password")


#########################################

is_egyptian = input ("Are you Egyptian? Type 'yes' or 'no' \n").lower()

if is_egyptian == "yes":
  
  print ("Good, that's the first step")
  is_18 = input ("Are you above 18? Type 'yes' or 'no' \n").lower()


  if is_18 == "yes":
   print ("You can have and ID")
  else:
   print ("Sorry, you have to be 18 or older")
   print ("Please try again when you are 18")


else:
 print ("Sorry, an Egyptian ID is give only to Egyptians")