import os


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def calculate_cost(quantity, price_per_item):
    return quantity * price_per_item

while True:
    clear_screen()
    budget = float(input("Enter your spending budget: "))
    item_name = input("Enter the item you want to buy: ")
    quantity = float(input(f"How many {item_name}s do you want to buy: "))
    price_per_item = float(input(f"Enter the price per {item_name}: "))
    
    total_cost = calculate_cost(quantity, price_per_item)
    
    if total_cost > budget:
        print("Warning: Your purchase exceeds your budget!")
    else:
        print("Purchase successful! Enjoy your new item.")
    
    if input("Do you want to continue? (y/n): ").lower() != "y":
        break