library = []
wished_books = []


first_book_owned = input("Enter the name of a book you own: ")
if first_book_owned:
    library.append(first_book_owned)

second_book_owned = input("Enter the name of another book you own (or press Enter to skip): ")
if second_book_owned:
    library.append(second_book_owned)

print(f"Your Library: {library}")


first_book_wished = input("Enter the name of a book you wish to have in the future: ")
if first_book_wished:
    wished_books.append(first_book_wished)

second_book_wished = input("Enter another wished book (or press Enter to skip): ")
if second_book_wished:
    wished_books.append(second_book_wished)

print(f"Your Wishlist: {wished_books}")


book_got = input("Enter the name of a book from your wishlist that you acquired (or press Enter to skip): ")

if book_got and book_got in wished_books:
    wished_books.remove(book_got)
    library.append(book_got)

print(f"Updated Library: {library}")
print(f"Updated Wishlist: {wished_books}")


book_donated = input("Enter the name of a book from your library you wish to donate (or press Enter to skip): ")

if book_donated and book_donated in library:
    library.remove(book_donated)

print(f"Final Library: {library}")
print(f"Final Wishlist: {wished_books}")