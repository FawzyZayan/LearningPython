import random

print("Welcome to 'Whose Wallet'")
print("You will give me a list of names, and I will pick a person to pay")

string_names = input("If you're ready, enter the names seperated by a comma: ")

names = string_names.split(", ")

random_choice = random.choice(names)

print(f"Please ask '{random_choice}' to take his wallet out. Dinner is on him!")