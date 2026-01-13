age = int (input ("Please enter your age \n"))
linceses = input ("Do you have linceses? Type (Yes)  or (No) \n")
if age >= 18 and linceses.lower() == "yes":
  print ("You can drive!")
elif age >= 18 or linceses.lower() == "no":
  print ("You can't drive")
else:
  print (f"You entery [ {linceses} ]  is not understood")