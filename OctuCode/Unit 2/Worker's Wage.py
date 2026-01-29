str_length = input("Please type Length: ")
str_width = input("Please type Width: ")
str_meter = input("How much for 1 meter: ")
length = float(str_length)
width = float(str_width)
str_area = length * width
area = float(str_area)
meter = float(str_meter)
dollars = area * meter
print("The total area is:", area)
print("Give the guy: $",dollars)