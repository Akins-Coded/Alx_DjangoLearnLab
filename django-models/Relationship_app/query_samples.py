

import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.LibraryProject.settings')  
django.setup()

# Import the models from the relationship_app
from relationship_app.models import Book, Author, Library

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        # Get the Author object by name
        author = Author.objects.get(name=author_name)
        # Retrieve all books by that author
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

def query_all_books():
    """
    List all books in the library.
    """
    books = Book.objects.all()
    print("All books in the library:")
    for book in books:
        print(f"- {book.title} by {book.author.name} (Published: {book.published_date})")

def query_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    """
    try:
        # Get the Library object by name
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Assuming one-to-one relationship to Librarian
        if librarian:
            print(f"The librarian for {library_name} is {librarian.name}")
        else:
            print(f"{library_name} does not have an assigned librarian.")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

if __name__ == '__main__':
   main()
