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
    ID = input("Enter the contact's ID: ")
    if ID.isdigit():
      name = input("Enter the contact's name: ")
      number = input("Enter the contact's number: ")
      if number.isdigit():
      
        contacts[ID] = {"Name": name, "Number": number}
        
        print(f"\n{name} was added successfully...\n")
      
      else:
        print("Enter a number...")
      
    else:
      print("Enter a number...")
      continue
  
  elif user_choice == 2:
    print(contacts)
    continue
  
  elif user_choice == 3:
    ID_to_edit = input("Enter the contact's ID to edit: ")
    if ID_to_edit.isdigit():
      if ID_to_edit in contacts:
        new_name = input("Enter the contact's name: ")
        new_number = input("Enter the contact's number: ")
        if new_number.isdigit():
        
          contacts[ID_to_edit] = {'Name': new_name, 'Number': new_number}
          
          
          print("\nSuccess...\n")
          
        else:
          print("Enter a number...")
          continue
      
      else:
        print(f"Sorry, {ID_to_edit} is not found...")
        continue
    
    else:
      print("Enter a number...")
    
  elif user_choice == 4:
    print("Exiting the Program...")
    break
    
  else:
    print("Invalid Input")
    continue