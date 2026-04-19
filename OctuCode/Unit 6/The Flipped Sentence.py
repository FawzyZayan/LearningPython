sentence = input("Enter a Scentence: ")
words = sentence.split()
flipped_words = words[::-1]
flipped_scentence = " ".join(flipped_words)
print(f"Flipped Scentence: "{flipped_scentence})