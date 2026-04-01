import time

print("*****Welcome to the Multiplication Table*****")

number = int(input("Enter a Number: "))

print("\nMultiplication in Progress...")

time.sleep(3)

print(f"\nMultiplicaton Table for {number}: \n")

for n in range(1,11):
  result = number * n
  print(f"{number} * {n} = {result}")