import random
print ("Welcome to the Coin Guessing Game!")
choice = input ("Choose a method to toss the coin: \n1. Using random.randint()\n2. Using random.random\nEnter your choice (1 or 2):")
if choice == '1':
  heads_or_tails = input ("Enter your Guess (Heads or Tails):").lower()
if heads_or_tails == 'heads':
  print ("Congratulations ! You won! \nthe computer's coin toss result was: Heads")
elif heads_or_tails == 'tails':
  print ("Sorry ! You lost! \nThe computer's coin toss result was: Heads")
if choice == '2':
  heads_or_tails = input ("Enter your Guess (Heads or Tails):").lower()
if heads_or_tails == 'heads':
  print ("Sorry ! You lost! \nThe computer's coin toss result was: Tails")
elif heads_or_tails == 'tails':
  print ("Congratulations ! You won! \nThe computer's coin toss result was: Tails")
else:
  print ("Invaled choice")