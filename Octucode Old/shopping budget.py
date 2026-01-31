import os
def clear():
  os.system("cls" if os.name == "nt" else "clear")
def calculate_total_cost(quantity, price_per_item):
  return quantity * price_per_item

while True:
  clear()

  budget = float(input("Enter your spending budget: "))
  item_name = input("Enter the name of the item you want to buy: ")
  quantity = int(input(f"How many {item_name}s do you want to buy: "))
  price_per_item = float(input(f"Enter the price per {item_name}: "))


  total_cost = calculate_total_cost(quantity,price_per_item)


  if total_cost > budget:
    print("Waring: Your purchase exeeds your budget.")
    to_continue = input("Do you want to continue y/n: ")
    if to_continue == "y":
      continue
    else:
      break
  else:
    print ("Success! Your purchase didn't exeeds your budget.")
    to_continue = input("Do you want to continue y/n: ")
    if to_continue == "y":
      continue
    else:
      break