from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Custom login view (if needed for token-based auth)
class LoginView(ObtainAuthToken):
    pass

# View for listing books
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for CRUD operations on books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Default permission for authenticated users

    def get_permissions(self):
        # Override to apply custom permissions
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.IsAuthenticatedOrReadOnly()]
        return [permission() for permission in self.permission_classes]
