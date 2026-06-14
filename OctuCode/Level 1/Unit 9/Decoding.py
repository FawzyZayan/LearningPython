import string

alphabet = string.ascii_lowercase
message = input("Please enter a Message: ")
shift_number = int(input("Enter a Shift Number: "))
decrypted_message = ""

for letter in message:
    if letter.lower() in alphabet:
        decrypted_position = alphabet.index(letter.lower())
        new_position = (decrypted_position - shift_number) % 26
        decrypted_letter = alphabet[new_position]

        if letter.isupper():
            decrypted_letter = decrypted_letter.upper()
        decrypted_message += decrypted_letter
    else:
        decrypted_message += letter


print(f"Here is the Original Message: {decrypted_message}")