total_seconds = int (input ("Enter the duration in seconds: \n")) 
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print (f"This duration is: {hours} hours, {minutes} minutes, and {seconds} seconds long.")