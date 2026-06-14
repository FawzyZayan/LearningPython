def information(name, age, number, nationality):
  print(f"Your name is {name}, you are {age} years old, your number is {number} and you are {nationality}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
number = int(input("Enter your number: "))
nationality = input("Enter your nationality: ")

information(name, age, number, nationality)