books = [ "Book 2", "Book 3", "Book 5" ]

books.insert(0, "Book 1")
books.insert(3, "Book 4")

# To add Book 6 I can make like this:
# books.insert(5, "Book 6")
# Or I can make like this:
# books.append("Book 6")
# Because Book 6 is the last element in the list

print(books)