items = []
prices = []
print ("\n***** Welcome to iShop calculator *****\n")
number_of_items = int (input ("How many items are there in your basket today: "))

if number_of_items > 0:
  for i in range (0, number_of_items):
        name = input(f"Please tell me the name of item number {i+1}: ")
        items.append(name)
        price = float (input (f"What is the price of {name}\n$"))
        prices.append(price)
else:
    print ("Seems like you're not in the mood for shopping today")

choice = input ("Would you like to see your entire basket items? ").lower()
if choice == "yes":
      print (items)
      see_price = input (
          "Would you like to see how much it'll cost? ").lower()
      if see_price == "yes":
        print ("\nBuying these items will cost: ")
        print (sum(prices))
      else:
        input ("Press enter to exit")
else:
  print ("Seems like you're not in the mood for shopping today")