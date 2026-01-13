import os

catalog = {}

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def AddBook():
    clear()
    ISBN = int(input ("Enter ISBN: "))
    title = input ("Enter title: ")
    author = input ("Enter author: ")
    catalog[ISBN] = {"Title": title, "Author": author, "Available": True}
    print (f"Book '{title}' by {author} added to the catalog with ISBN {ISBN}")

def BookCheckOut():
    clear()
    check_out_ISBN = int(input("Enter ISBN to check out: "))
    if check_out_ISBN in catalog:
        if catalog[check_out_ISBN]['Available'] == True:
            catalog[check_out_ISBN]['Available'] = False
            print (f"Book '{catalog[check_out_ISBN]['Title']}' checked out")
        else:
            print("This book is already checked out")
    else:
        print ("We don't have this ISBN in the catalog")

def BookCheckIn():
    clear()
    check_in_ISBN = int(input("Enter ISBN to check in: "))
    if check_in_ISBN in catalog:
        if catalog[check_in_ISBN]['Available'] == False:
            catalog[check_in_ISBN]['Available'] = True
            print (f"Book '{catalog[check_in_ISBN]['Title']}' checked in")
        else:
            print("This book is already checked in")
    else:
        print ("We don't have this ISBN in the catalog")
    
while True:
    print("""
     Menu:
     1. Add book
     2. Check out book
     3. Check in book
     4. List books 
     5. Exit
     """)

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        AddBook()
        y_n = input ("Do you want to add another book? (y/n): ")

        while "y" in y_n:
            AddBook()
            y_n = input ("Do you want to add another book? (y/n): ")

        if y_n != "y":
            continue

    elif  choice == 2:
        BookCheckOut()
        y_n = input ("Do you want to check out another book? (y/n): ")

        while "y" in y_n:
            BookCheckOut()
            y_n = input ("Do you want to check out another book? (y/n): ")

        if y_n.lower() != "y":
            continue

    elif  choice == 3:
        BookCheckIn()
        y_n = input ("Do you want to check in another book? (y/n): ")

        while "y" in y_n:
            BookCheckIn()
            y_n = input ("Do you want to check in another book? (y/n): ")

        if y_n.lower() != "y":
            continue

    elif choice == 4:
        clear()
        print("Library Catalog:")
        for ISBN, book_info in catalog.items():
            print(f"ISBN: {ISBN}, Title: {book_info['Title']}, Author: {book_info['Author']}, Available: {book_info['Available']}")

    elif choice == 5:
        print("Exiting....")
        break

    else:
        print("Invalid choice")
        continue
