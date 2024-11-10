# Delete Operation
from bookshelf.models import Book
Command:
```python
retrieved_book.delete()
all_books = Book.objects.all()
print(all_books)  # Should return an empty queryset
