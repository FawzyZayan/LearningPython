import string

def dencrypt(message, shift):
  alphabet = string.ascii_lowercase
  dencrypted_message = ""

  for letter in message:
    if letter.lower() in alphabet:
       original_position = alphabet.index(letter.lower())
       new_position = (original_position - shift) % 26
       dencrypted_letter = alphabet[new_position]
       if letter.isupper():
          dencrypted_letter = dencrypted_letter.upper()
       dencrypted_message += dencrypted_letter
    else:
        dencrypted_message += letter
  print(f"\n\nHere is the original message\n\n*****\n\n{dencrypted_message}\n\n*****")


user_message = input("Enter a message: ")
shift_number = int(input("Enter a shift number: "))


dencrypt(message = user_message, shift = shift_number)