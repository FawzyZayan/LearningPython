total_seconds = int(input("Enter the duration in seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds  % 60
print("The duration is: ", hours, "hours,", minutes, "minutes and", seconds, "seconds")