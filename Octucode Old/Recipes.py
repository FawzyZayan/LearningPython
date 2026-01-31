import time

class Recipe:
    def __init__(self, name, ingredients, time, instructions):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = time
        self.instructions = instructions

    def display(self):
        print("Displaying Recipe ....\n")
        time.sleep(3)
        print(f"Name: {self.name}\n")
        print(f"Ingredients: {self.ingredients}\n")
        print(f"Time: {self.cooking_time}\n")
        print(f"Instructions: {self.instructions}\n")

def order():
    print("Welcome to Recipe Collection\n")
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ")
    cooking_time = input("Enter cooking time: ")
    instructions = input("Enter cooking instructions: ")

    return Recipe(name, ingredients, cooking_time, instructions)

food = order()
food.display()