import string

alphabet = string.ascii_lowercase
message = input("Please enter a Message: ")
shift_number = int(input("Enter a Shift Number: "))
original_message = ""

for letter in message:
    if letter.lower() in alphabet:
        original_position = alphabet.index(letter.lower())
        new_position = (original_position - shift_number) % 26
        original_letter = alphabet[new_position]

        if letter.isupper():
            original_letter = original_letter.upper()
        original_message += original_letter
    else:
        original_message += letter


print(f"Here is the Original Message: {original_message}")