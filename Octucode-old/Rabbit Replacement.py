print ("Welcome to place the RABBIT\n")

field = [ ["🌿","🌿","🌿"], ["🌿","🌿","🌿"], ["🌿","🌿","🌿"] ]

print (f"{field[0]}\n{field[1]}\n{field[2]}\n")

print ("Where should the RABBIT go? 🐇\n")

position = input ("Please, enter a row and a column: ")

row = int(position[0]) -1
column = int(position[1]) -1
field[row][column] = "🐇"
print ("\n Success .....\n")

print (f"{field[0]}\n{field[1]}\n{field[2]}\n")