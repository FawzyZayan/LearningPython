contacts = {}

while True:
  print("Contact Management")
  user_choice = int(input("""
  1- Add Contact
  2- View Contact
  3- Edit a Contact
  4- Exit

  Please choose a nuber from 1 to 4: """))

  if user_choice == 1:
    contacts["ID"] = ID = input("Enter the contact's ID: ")
    contacts["name"] = name = input("Enter the contact's name: ")
    contacts["number"] = number = int(input("Enter the contact's number: "))
    
    print(f"\n{name} was added successfully...\n")
    continue
  
  elif user_choice == 2:
    print(contacts)
    continue
  
  elif user_choice == 3:
    contacts["ID"] = ID = input("Enter the contact's ID: ")
    contacts["name"] = name = input("Enter the contact's name: ")
    contacts["number"] = number = int(input("Enter the contact's number: "))
    print("\nSuccess...\n")
    continue
  
  elif user_choice == 4:
    print("Exiting the Program...")
    break
    
  else:
    print("Invalid Input")