import string

alphabet = string.ascii_lowercase
message = input("Please enter a Message: ")
shift_number = int(input("Enter a Shift Number: "))
encrypted_message = ""

for letter in message:
    if letter.lower() in alphabet:
        original_position = alphabet.index(letter.lower())
        new_position = (original_position + shift_number) % 26
        encrypted_letter = alphabet[new_position]

        if letter.isupper():
            encrypted_letter = encrypted_letter.upper()
        encrypted_message += encrypted_letter
    else:
        encrypted_message += letter


print(f"Here is the Encrypted Message: {encrypted_message}")
