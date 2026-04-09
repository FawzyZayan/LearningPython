numbers = [ 1,2,3,4,5 ]
total = 0

print("Let's add each number to the next:")

for number in numbers:
  total += number
  print(f"-> {total}")
  print(f"\nThe total number is: {total}")