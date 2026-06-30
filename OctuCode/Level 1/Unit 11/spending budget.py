import os


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")

def buying():
    while True:
        clear_screen()
        budget = int(input("Enter your spending budget: "))
        item = input("Enter the item you want to buy: ")
        how_many = int(input(f"How many {item}s you want to buy: "))
        per = int(input(f"Enter the price per {item}: "))
        price = how_many * per
        if budget < price:
            print("Warning: Your purchase exceeds your budget!")
        else:
            print("Purchase successful! Enjoy your new item.")
        y_n = input("Do you want to continue? (y/n): ").lower()
        if y_n != "y":
            print("Goodbye!")
            break


buying()