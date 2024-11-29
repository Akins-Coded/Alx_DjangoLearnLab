from rest_framework import generics, filters  
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
# from django_filters import rest_framework   CODED-SOMETHING

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for all users
    filter_backends = [filters.OrderingFilter] 
    ordering_fields = ['title', 'author'] # Configuring Ordering fields to allow key-words from title or author

    def get_queryset(self):
        title = self.kwargs['title'] 
        return Book.objects.filter(book__title=title)
    
    def get_queryset(self):
        author = self.kwargs['author'] 
        return Book.objects.filter(book__author=author)
    
    def get_queryset(self):
        publication_year = self.kwargs['publication_year'] 
        return Book.objects.filter(book__publication_year=publication_year)
# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for all users

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
    
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

    def perform_update(self, serializer):
        serializer.save()


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only
