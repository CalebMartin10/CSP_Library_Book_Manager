class Book:
    """
    This class creates the blueprint for creating and storing books.

    Args:
      title (str): The name of the book.
      author (str): the name of the author.
      isbn (int): the ISBN for the book.
    """
    def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
    
    def __str__(self):
          """
          This method prints a formatted report of a book so print statements print nicely.

          Args:
            title (str): The name of the book.
            author (str): the name of the author.
            isbn (int): the ISBN for the book.
          """
          return (
                f"--------------------------\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
                f"--------------------------"
          )
    
    def __repr__(self):
          """
          This method prints a formatted report of a book so that print statement iterating over lists can print nicely.

          Args:
            title (str): The name of the book.
            author (str): the name of the author.
            isbn (int): the ISBN for the book.
          """
          return (
                f"--------------------------\n"
                f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"ISBN: {self.isbn}\n"
          )
    
    def get_details(self):
          return print(self)

if __name__ == "__main__":
    my_favorite_book = Book("Christmas Carol", "Charles Dickens", 9781912714704)
    Book.get_details(my_favorite_book)
    input("Press Enter to Exit")