import string
alphabet = string.ascii_lowercase
space = " "
punctuation = string.punctuation
numberd = string.digits
word = input("Please type a word: ").lower()
encrypted_word = ""
for letter in word:
  if letter in alphabet:
    original_position = alphabet.index(letter)
    new_position = (original_position + 2) % 26
    encrypted_word = encrypted_word + alphabet[new_position]
    #encrypted_word += alphabet[new_position]
  else:
    #encrypted_word += letter
    encrypted_word = encrypted_word + letter

print (f"Here is the encrypted word: {encrypted_word}")
