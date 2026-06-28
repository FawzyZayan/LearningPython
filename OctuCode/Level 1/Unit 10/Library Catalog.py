import os

library_catalog = {}

def clear_screen():
  os.system("cls") if os.name == "nt" else os.system("clear")
  
def add_book():
  while True:
    clear_screen()
    ISBN = input("Enter ISBN: ")
    if ISBN.isdigit():
      title = input("Enter Title: ")
      author = input("Enter Author: ")
      
      library_catalog[ISBN] = {"Title": title,
                              "Author": author,
                              "Available": True}
      
      print(f"\nBook '{title}' by {author} was added to the Library Catalog with ISBN {ISBN}.\n")
      y_n = input("Do you want to add another book? (y/n): ").lower()
      if y_n != "y":
        print("\n")
        break
    else:
      print("\nEnter a number.\n")
      break
    
def check_out_book():
  while True:
    clear_screen()
    ISBN = input("Enter ISBN to check out: ")
    if ISBN.isdigit():
      if ISBN in library_catalog:
        if library_catalog[ISBN]["Available"]:
          library_catalog[ISBN]["Available"] = False
          print(f"\nBook '{library_catalog[ISBN]["Title"]}' Checked Out successfully\n")
          y_n = input("Do you want to check out another book? (y/n): ").lower()
          if y_n == "y":
            print("\n")
            break
        else:
          print("\nSorry, the book is currently checked out.\n")
          y_n = input("Do you want to check out another book? (y/n): ").lower()
          if y_n != "y":
            print("\n")
            break
      else:
        print("\nBook not found in the Library Catalog.\n")
        y_n = input("Do you want to check out another book? (y/n): ").lower()
        if y_n != "y":
          print("\n")
          break
    else:
      print("\nPlease enter a Number.\n")
      y_n = input("Do you want to check out another book? (y/n): ").lower()
      if y_n != "y":
        print("\n")
        break
      
def check_in_book():
  while True:
    clear_screen()
    ISBN = input("Enter ISBN to check in: ")
    if ISBN.isdigit():
      if ISBN in library_catalog:
        if not library_catalog[ISBN]["Available"]:
          library_catalog[ISBN]["Available"] = True
          print(f"\nBook '{library_catalog[ISBN]["Title"]}' Checked In successfully.\n")
          y_n = input("Do you want to check In another book? (y/n): ").lower()
          if y_n != "y":
            print("\n")
            break
        else:
          print("\nSorry, the book is currently in the Library Catalog.\n")
          y_n = input("Do you want to check in another book? (y/n): ").lower()
          if y_n != "y":
            print("\n")
            break
      else:
        print("\nBook not found in the Library Catalog.\n")
        y_n = input("Do you want to check in another book? (y/n): ").lower()
        if y_n != "y":
          print("\n")
          break
    else:
      print("\nPlease enter a Number.\n")
      y_n = input("Do you want to check in another book? (y/n): ").lower()
      if y_n != "y":
        print("\n")
        break
      
def list_books():
  clear_screen()
  print("Library Catalog:\n")
  for ISBN in library_catalog:
    book_info = library_catalog[ISBN]
    print(f"ISBN: {ISBN}, Title: {book_info["Title"]}, Author: {book_info["Author"]}, Available: {book_info["Available"]}\n")

while True:
  print("Menu:")
  print("1. Add Book")
  print("2. Check Out Book")
  print("3. Check In Book")
  print("4. List Books")
  print("5. Exit")
  choice = input("Enter your Choice (1-5): ")
  
  if choice == "1":
    add_book()
  elif choice == "2":
    check_out_book()
  elif choice == "3":
    check_in_book()
  elif choice == "4":
    list_books()
  elif choice == "5":
    print("\nExiting the Program...")
    break
  else:
    print("\nPlease Follow the Rules.\n")
    continue