
import os
import django

# Set up the Django environment (assuming you have set your DJANGO_SETTINGS_MODULE correctly)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')  # Change this to your actual settings module
django.setup()

from relationship_app.models import Book, Author, Library

def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
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
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        if librarian:
            print(f"The librarian for {library_name} is {librarian.name}")
        else:
            print(f"{library_name} does not have an assigned librarian.")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

if __name__ == '__main__'