import time

name = input("Enter a user name: ")
email = input("Enter your email: ")

if "@" in email and "." not in email:

  time.sleep(3)
  print("Checking user name .....")
  time.sleep(3)
  print("Validating email address .....")
  time.sleep(3)
  print("Invaled email format. Registration failed.")
elif "." in email and "@" not in email:

  time.sleep(3)
  print("Checking user name .....")
  time.sleep(3)
  print("Validating email address .....")
  time.sleep(3)
  print("Invaled email format. Registration failed.")

else:
  time.sleep(3)
  print("Checking user name .....")
  time.sleep(3)
  print("Validating email address .....")
  time.sleep(3)
  print(f"User '{name}' with email '{email}' successfully added")