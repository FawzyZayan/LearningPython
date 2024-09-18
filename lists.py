fruit_basket = ["Apples" , "Oranges" , "Bananas"]
guess = input ("Guess the name of the fruits in the basket: ")

if guess in fruit_basket:
    print ("Good guess")
else:
    print ("Sorry, better luck next time")