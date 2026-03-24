print("Welcome to Place the Rabbit")

list1 = ["🍀", "🍀", "🍀"]
list2 = ["🍀", "🍀", "🍀"]
list3 = ["🍀", "🍀", "🍀"]

print(list1)
print(list2)
print(list3)

print("\n")

print("Where should the Rabbit go 🐇 \n")

row_and_column = input("Please enter a Row and a Column: ")


if row_and_column == "11":
  print("\nSuccess... \n")
  print("""
        ["🐇", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
""")
  
elif row_and_column == "12":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🐇", "🍀"]
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
""")
  
elif row_and_column == "13":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🐇"]
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
""")
  
elif row_and_column == "21":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🍀"]
        ["🐇", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
""")
  
elif row_and_column == "22":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🍀"]
        ["🍀", "🐇", "🍀"]
        ["🍀", "🍀", "🍀"]
""")
  
elif row_and_column == "23":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🐇"]
        ["🍀", "🍀", "🍀"]
""")
  
elif row_and_column == "31":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
        ["🐇", "🍀", "🍀"]
""")
  
elif row_and_column == "32":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
        ["🍀", "🐇", "🍀"]
""")
  
elif row_and_column == "33":
  print("\nSuccess... \n")
  print("""
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🍀"]
        ["🍀", "🍀", "🐇"]
""")
  
else:
  print("\nPlease enter a Row and a Column")