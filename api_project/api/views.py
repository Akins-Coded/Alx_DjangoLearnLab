from rest_framework.generics.ListAPIView import ListAPIView
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(ListAPIView):
    BookList = Book.objects.all()
    serializer_class = BookSerializer
    
