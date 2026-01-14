total_seconds = input("Please type the number of seconds: ")
int_seconds = int(total_seconds)
hours = int_seconds // 3600
minutes = int_seconds % 60
seconds = int_seconds % 1
print(total_seconds, "seconds equals", hours, "hours,", minutes, "minutes and", seconds, "seconds")