import time
import sys

items = [  ]
prices = [  ]

print("***** Welcome to iShop Calculator *****\n")
number_of_items = int(input("How many items are there in your basket today: "))

if number_of_items > 0:
  print("\nLet's get on counting them...")
  time.sleep(3)
  for n in range(0, number_of_items):
    item_name = input(f"What's the name of item {n+1}: ")
    items.append(item_name)
    item_price = float(input(f"What's the price of {item_name}\n⃁"))
    prices.append(item_price)
    
choice = input("Would you like to see the entire basket? (Yes or No): ").capitalize()
if choice == "Yes":
  print(items)
  see_price = input("Would you like to see how much it'll cost? (Yes or No): ").capitalize()
  if see_price == "Yes":
    print("\nBuying these items will cost: ")
    print(sum(prices))
    
  elif see_price == "No":
    sys.exit(0)
  
  else:
    sys.exit(0)
elif choice == "No":
  see_price = input("Would you like to see how much it'll cost? (Yes or No): ").capitalize()
  if see_price == "Yes":
    print("\nBuying these items will cost: ")
    print(sum(prices))
    
  elif see_price == "No":
    sys.exit(0)
  
  else:
    sys.exit(0)
else:
  sys.exit(0)