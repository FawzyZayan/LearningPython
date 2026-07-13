import time

user_name = input("Enter your user name: ")
email = input("Enter your email: ")

print("Checking user name...")
time.sleep(2)

if "@" in email and "." in email:
    print("Validating email address...")
    time.sleep(2)
    
    if user_name.isdigit():
        print("Please enter a name not a number")
    else:
        print(f"User '{user_name}' with email '{email}' successfully added.")
else:
    print("Invalid email format. Registration Failed.")
