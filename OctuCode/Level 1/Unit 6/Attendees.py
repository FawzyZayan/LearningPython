import sys

attendees_input = input("Enter the Names of the Attendees seperated by a comma: ")
attendees = attendees_input.split(", ")
for person in attendees:
  print(person)
  yes_or_no = input("Is this Person Attending? (Yes or No): ").capitalize()
  if yes_or_no == "Yes":
    print("Attendance Confirmed!")
  elif yes_or_no == "No":
    print("Attendance Not Confirmed!")
  else:
    print("Please Follow the Rules")
    sys.exit(0)
  
  print("----------")