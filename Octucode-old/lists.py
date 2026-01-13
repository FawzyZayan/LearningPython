fruit_basket = ["Apples" , "Oranges" , "Bananas"]
guess = input ("Guess the name of the fruits in the basket: ")

if guess in fruit_basket:
    print ("Good guess")
else:
    print ("Sorry, better luck next time")


#############################################

basket = [ ["Apples","Bananas"], ["Milk", "Water"] ]
print(basket)
input("Press enter to change the content ..... ")


basket[0].insert(0,"Oranges")
basket[0].append("Kiwis")
basket[1].remove("Water")
basket[1].insert(0,"Coffee")
basket[1].append("Tea")
basket.append([1,2,3])


print ("Here is the updated basket")
print(basket)