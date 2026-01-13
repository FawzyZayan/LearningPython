tasks_list = input(
    "Enter your tasks for today seperated by a comma: ").split(", ")
done_tasks = []
ongoing_tasks = []

for task in tasks_list:
    print (f"\n{task}\n")
    done = input (f"Did you finish {task} already? \n").lower()
    if done == "yes":
      print ("Nice Job")
      done_tasks.append(task)
    else:
      print ("Try not to put it off")
      ongoing_tasks.append(task)
    print ("_______________")
see_progress = input ("Do you want to see your today's progress?(yes, no)\n")
if see_progress == "no":
  input ("Please hit Enter to exit")
else:
  print ("""
           ******** Done Tasks ********
           """)
  print(done_tasks)

  print ("""
           ******** Ongoing Tasks ********
          """)
  print (ongoing_tasks)