import random
import time
import os

def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    results = {
        "draw": "Draw 😊 \n\n",
        "user_over": "You went over 21, Sorry 🫢 \n\n",
        "computer_over": "The computer went over 21, You win ⭐️ \n\n",
        "user_21": "You won with a blackjack, 😎👌🏻🔥 \n\n",
        "computer_21": "The computer won with a blackjack, 😱 \n\n",
        "user_won": "You won, 🥰 \n\n",
        "user_lose": "You lose, 😢 \n\n",
    }

    if user_score == computer_score:
        return results["draw"]
    elif user_score > 21:
        return results["user_over"]
    elif computer_score > 21:
        return results["computer_over"]
    elif user_score == 0:
        return results["user_21"]
    elif computer_score == 0:
        return results["computer_21"]
    elif user_score > computer_score:
        return results["user_won"]
    else:
        return results["user_lose"]

def game():
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    game_continue = True
    while game_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print (f"\n\n\nYour cards are {user_cards}, current score is {sum(user_cards)}")
        print (f"Computer's first card is {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:
            game_continue = False
        else:
            user_needs_another_card = input("Get another card? y/n: ").lower()
            if user_needs_another_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                game_continue = False

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} with score {user_score}")
    time.sleep(3)
    print(f"Computer's final hand: {computer_cards} with score {computer_score}")
    print(compare(user_score, computer_score))
    time.sleep(3)
    clear()


while input("Choose a game to start .....\n\n1- Froggy \n2- Twenty one \n3- Snake \n").lower() == "twenty one":
    clear()
    game()