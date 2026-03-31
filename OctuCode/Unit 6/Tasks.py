import sys

finished_tasks = []
ongoing_tasks = []

tasks = input("Enter your Tasks seperated by a comma: ").split(", ")

for task in tasks:
  finished = input(f"Did you Finish {task}? (Yes or No): ").capitalize()
  if finished == "Yes":
    print("\nNice Job!\n")
    print("-----")
    finished_tasks.append(task)
  elif finished == "No":
    print("\nDon't Put It Off\n")
    print("-----")
    ongoing_tasks.append(task)
  else:
    print("Please Follow the Rules")
    sys.exit(0)

viewing_lists = input("Do you want to See your Progress? (Yes or No): ").capitalize()

if viewing_lists == "Yes":
  print("Finished Tasks:")
  print(finished_tasks)
  print("\n")
  print("Omgoing Tasks:")
  print(ongoing_tasks)
elif viewing_lists == "No":
  input("Press Enter to Exit...")
else:
  ("Please Follow the Rules")
  sys.exit(0)