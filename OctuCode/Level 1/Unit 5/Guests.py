guests = ["Ramy", "Mohammed", "Ahmed", "Nora"]

name = input("Enter a name: ").capitalize()

if name in guests:
  print(f"Great, {name} was in the list!")

else:
  print(f"Oh uh, {name} wasn't in the list!")