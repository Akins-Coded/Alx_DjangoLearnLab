from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookList(request):
    BookList = Book.objects.all()
    serializer_class = BookSerializer
    
