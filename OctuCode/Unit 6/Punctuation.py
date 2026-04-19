import string

scentence = input("Enter a Scentence with Punctuation: ")
new_scentence = ""

for word in scentence:
  if word not in string.punctuation:
    new_scentence += word
    
print("\n\n *** Here is the Sentence Without Punctuation *** \n\n", new_scentence)