print ("\n*** Welcome to the Multiplication Table ***")
number = int (input ("Enter a number: "))
print (f"\nMultiplication table for {number}: \n")
for l in range(1,11):
  result = number * l
  print (f"{number} x {l} = {result}")