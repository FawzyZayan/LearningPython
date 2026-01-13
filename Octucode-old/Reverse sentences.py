sentence = input ("Enter a sentence: ")
words = sentence.split()
revesed_words = (words[::-1])
print (revesed_words)
reversed_sentence = " ".join(revesed_words)


print ("Reversed sentence:", reversed_sentence)