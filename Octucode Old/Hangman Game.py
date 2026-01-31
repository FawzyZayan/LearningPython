import random
hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = ["good", "bad", "ugly"]
random_word = random.choice(words)
display = ["_"] * len(random_word)

print (" ".join(display))
print (hangman_stages[0])

lives = 6
guessed_letters = []

while "_" in display and lives > 0:
  guessed = input ("Please guess a letter: ").lower()

  if guessed in guessed_letters:
    print ("You have already guessed that. Try again")
    print (f"You have {lives} more tries")
    
    continue
   
  guessed_letters.append(guessed)

  if guessed not in random_word:
    lives -= 1
    print (hangman_stages [6 - lives])

  else:
    for position in range (len (random_word)):
      if random_word [position] == guessed:
        display [position] = guessed
  print (" ".join(display))
  print (f"You have {lives} more tries")


if lives == 0:
  print ("""
         You lose!
         """)
  print (f"{hangman_stages[-1]}\n")
  print (f"The word is: {random_word}")

else:
  print ("""
         **********
         YOU WIN!
         **********
         """)