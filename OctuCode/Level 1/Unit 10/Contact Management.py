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
    if ID.isdigit():  
      contacts["name"] = name = input("Enter the contact's name: ")
      contacts["number"] = number = input("Enter the contact's number: ")
      
      print(f"\n{name} was added successfully...\n")
    else:
      print("Enter a number...")
      continue
  
  elif user_choice == 2:
    print(contacts)
    continue
  
  elif user_choice == 3:
    ID_to_edit = input("Enter the contact's ID to edit: ")
    if ID_to_edit in contacts["ID"]:
      contacts["name"] = new_name = input("Enter the contact's name: ")
      contacts["number"] = new_number = int(input("Enter the contact's number: "))
      print("\nSuccess...\n")
    
    else:
      print(f"Sorry, {ID_to_edit} is not found...")
      continue
    
  elif user_choice == 4:
    print("Exiting the Program...")
    break
    
  else:
    print("Invalid Input")