username = input("Please enter your username: ")
password = input("Please enter your password: ")
print("Oops! Logged out! We are sorry it's an error from us, we are working to fix it, please wait... there all done. Log in again please")
log_in_username = input("Please enter your username: ")
log_in_password = input("Please enter your password: ")
if log_in_username == username and log_in_password == password:
  print("Welcome to the app!")
else:
  print("Invalid username or password. Try again")