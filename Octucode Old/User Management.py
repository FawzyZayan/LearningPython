import os
import time

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def printing():
    print("\nWelcome to User Management\n\n")
    print("Choose an Action:\n")
    print("""
    1. Add new user
    2. Display all users
    3. Exit""")


def taking(users):
    while True:

        printing()
        one_two_three = int(input("Enter your choice: "))
        if one_two_three == 1:
            first = input("Enter your first name: ")
            last = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            print("User added successfully")
            time.sleep(3)
            user = (first, last, email, password)
            users.append(user)
            clear()
        elif one_two_three == 2:
            print("Displaying all users...")
            time.sleep(3)
            print(users)
            print("______________________________")
            time .sleep(5)
            clear()
        elif one_two_three == 3:
            print("Exiting...")
            time.sleep(3)
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(3)
            clear()
            printing()
            taking(users)


users = []
taking(users)