# Create Operation
from .models import Book


# Create a new Book instance using the create method
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output comment: Book instance created successfully.

