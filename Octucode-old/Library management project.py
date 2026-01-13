library = []
wishlist = []
donations = []

book_name = input ("Enter the name of a book you own: ")
library.append(book_name)

book_name = input ("Enter the name of another book you own (or press 'Enter' to skip): ")
if book_name:
    library.append(book_name)

print ("\nYour Library: ", library)

book_name = input ("\nEnter the name of a book you wish to have in the future: ")
wishlist.append(book_name)
book_name = input ("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if book_name:
  wishlist.append(book_name)

print ("\nYour Wishlist: ", wishlist)

acquired_book = input ("\nEnter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if acquired_book in wishlist:
  library.append(acquired_book)
  wishlist.remove(acquired_book)

print ("\nUpdated Library: ", library)
print ("Updated Wishlist: ", wishlist)

donated_book = input ("\nEnter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donated_book in library:
  donations.append(donated_book)
  library.remove(donated_book)

print ("\nFinal Library after Donations: ", library)
print ("\nFinal Wishlist after Donations: ", wishlist)
print ("\nFinal Donations after Donations: ", donations)