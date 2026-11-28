class Recipe:
  def __init__(self, name, ingredients, instructions, time):
    self.name = name
    self.ingredients = ingredients
    self.instructions = instructions
    self.time = time
    
  def display(self):
    print(f"Name: {self.name}")
    print(f"Ingredients: {self.ingredients}")
    print(f"Instructions: {self.instructions}")
    print(f"Time: {self.time}")
    
    
def recipe():
  name = input("Enter Recipe's Name: ")
  ingredients = input("Enter Recipe's Ingredients (comma-seperated): ")
  instructions = input("Enter Cooking Instructions: ")
  time = input("Enter Cooking Time: ")
  
  return Recipe(name, ingredients, instructions, time)

print("Welcome to Recipe Collection\n")

recipe1 = recipe()
print("Recipe added successfully\n")

print("Displaying Recipe...")
recipe1.display()