is_egyptian = input("Are you Egyptian type 'Yes' or 'No': ").lower()

if is_egyptian == "yes":
  print("Great, this is the first step")
  age = int(input("How old are you: "))
  
  if age >= 18:
    print("Great, you can have an Egyptian ID Card")
  else:
    print("Sorry, you need to be 18 or older")
    print("Please try again when you are 18 or older")
elif is_egyptian == "no":
  print("Only Eguptians can get an Egyptian ID Card")
else:
  print("Please follow the instructions")