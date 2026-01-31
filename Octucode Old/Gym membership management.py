import os
import time

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def printing():
    print("\nWelcome to Gym Membership Management\n\n")
    print("Choose an Action:\n")
    print("""
    1. Add new member
    2. Display all members
    3. Search for a member
    4. Exit""")

def search_nested(mylist, val):
    results = []
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            if mylist[i][j] == val:
                # return mylist[i]
                results.append(mylist[i])

    if results == []:
        return "Not Found!"

    return results


def taking(members):
    while True:

        def __init__(self, first, last, ID, status):
            self.first = first
            self.last = last
            self.ID = ID
            self.status = status

        printing()
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            ID = int(input("Enter membership ID: "))
            status = input("Enter membership status, Or click enter: ").lower()
            if status == "active":
                print("User added successfully")
                time.sleep(3)
                member = (first, last, ID, status)
                members.append(member)
                clear()
            else:
                print("User added successfully")
                time.sleep(3)
                member = (first, last, ID, "inactive")
                members.append(member)
                clear()

        elif user_choice == 2:
            if members == []:
                clear()
                print("Sorry, there is no thing to print. List is empty")
                time.sleep(3)

            else:
              print("Displaying all members...")
              time.sleep(3)
              print(members)
              print("_" * 20)
              time .sleep(5)
            
            
        elif user_choice == 3:
            clear()
            user_input = input("Enter what you want to search for: ")
            print(search_nested(members, user_input))
            time.sleep(5)
            clear()
            
        else:
            print("Exiting...")
            time.sleep(3)
            break

members = []
taking(members)

#1. update search to get all data