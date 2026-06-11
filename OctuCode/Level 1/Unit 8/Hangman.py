import random

HANGMANPICS = [
    """
    +---+
        |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """,
]

words = ["panda", "office", "cabin", "basement"]
random_word = random.choice(words)
tries = 6
guessed_letters = []


display = []
display = ["_"] * len(random_word)
print(" ".join(display))
print(HANGMANPICS[0])


while "_" in display and tries > 0:
    guessed = input("Guess a Letter: ").lower()
    
    if guessed in guessed_letters:
        print("You entered this letter before. Try again.")
        print(f"You have {tries} tries left")
        continue
    guessed_letters.append(guessed)

    if guessed not in random_word:
        tries -= 1
        print(HANGMANPICS[6 - tries])
        
    
    else:
        for position in range(len(random_word)):
            if random_word[position] == guessed:
                display[position] = guessed
        
    print(" ".join(display))
    print(f"You have {tries} tries left.")

    
if tries == 0:
    print("You Lose!")
    print(HANGMANPICS[-1])
    print(f"The word was {random_word}")
    
else:
    print("You Win!")