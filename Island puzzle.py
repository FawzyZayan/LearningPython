print ("Welcome to my island")

choosen_door = input("There are two doors in front of you. 🚪 a (red) door and 🚪 a (blue) door \n Which door do you want to open? \n").lower()

if choosen_door == 'blue':
    print("Oops! You open the crocodile door. \n Game over 🐊🐊🐊")
elif choosen_door == 'red':
    choosen_box = input("Great! now you entered a room. \n you found three boxes: (🎁 white), (🎁 black), (🎁 green)\n choose one :").lower()


    if choosen_box == 'white':
        print("Oops, you opened a box filled with spiders 🕷️🕷️🕷️. \n Game over")
    elif choosen_box == 'black':
        print("Oops, you opend a box filled with snakes. \n Game over🐍🐍🐍")
    elif choosen_box == 'green':
        print("Congratulations, you found the treasure. \n You won 💰💰💰")
    else:
        print("Invaled choice ‍🤷🏻‍♂️🤷🏻‍♂️🤷🏻‍♂️ ")
