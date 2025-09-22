import book
my_library = []

def add_book(library):
    """
    Creates and Adds a book to User's choice list.

    Args:
        library (list): A list of the Users choosing.
    """
    title = input(f"Book Title: ")
    author = input(f"Author's Name: ")
    isbn = input(f"ISBN: ")
    library.append(book.Book(title, author, isbn))
    return

def list_books(library):
    """
    Finds all books contained within a list.

    Args:
        library (list): A list of the Users choosing.
    
    Returns:
        All books formatted under the book.py __str__ method.
    """
    return print([book for book in library])

def find_book(library, query):
    """
    Finds all books with a certain title or author.

    Args:
        library (list): A list of the Users choosing.
        query (str): A name of a book or author.
    
    Returns:
        All books with the name or author formatted under the book.py __str__ method.
    """
    return print([book if query == book.title or query == book.author else "No results found" for book in library])

if __name__ == "__main__":
    """
    Creates the main logic of the program which allows users to add, find books in, look over, a list or exit the program.

    Args:
        library (list): A list of the Users choosing.
        query (str): A name of a book or author.
    """
    while True:
        response = input("\nType in what you want to do (Answer is case sensitive)...\n"
                         "Add a new book\n"
                         "List all books\n"
                         "Find a book\n"
                         "Exit the program\n"
                         " \n")
        if response == "Add a new book":
            add_book(my_library)
        elif response == "List all books":
            print(" ")
            list_books(my_library)
            print(" ")
        elif response == "Find a book":
            query = input(f"Type in the name or author of the book you are looking for: ")
            find_book(my_library, query)
        elif response == "Exit the program":
            break
        else:
            print("You need to type in the response exactly (Caps and specific spacing)")
            continue