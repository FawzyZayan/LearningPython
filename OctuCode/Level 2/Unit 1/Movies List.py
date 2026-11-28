class Movie:
  def __init__(self, title, director, year, genre):
    self.title = title
    self.director = director
    self.year = year
    self.genre = genre
    
  def display(self):
    print(f"Title: {self.title}")
    print(f"Director: {self.director}")
    print(f"Release Year: {self.year}")
    print(f"Genre: {self.genre}")
    print("\n")
    
    
first_movie = Movie("Inception", "Christopher Nolan", "2010", "Sci-Fi")
second_movie = Movie("THe Godfather", "Francis Ford Coppola", "1972", "Crime")
third_movie = Movie("Parasite", "Bong Joon-ho", "2019", "Thiller")

print("Movie List\n")

first_movie.display()
second_movie.display()
third_movie.display()

print("Changing Movie Directors...\n")

print("First Movie Details:\n")
first_movie.director = "Shokry Sarhan"
first_movie.display()

print("Second Movie Details:\n")
second_movie.director = "Ahmed Mazhar"
second_movie.display()

print("Third Movie Details:\n")
third_movie.director = "Isamel Yassin"
third_movie.display()