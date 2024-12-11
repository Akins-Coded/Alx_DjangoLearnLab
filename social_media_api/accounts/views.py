from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer

CustomUser = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for retrieving user information (read-only).
    Requires authentication to access.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Added permission class

class RegisterView(generics.CreateAPIView):
    """
    API endpoint for user registration.
    Returns a token upon successful registration.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_header(serializer.data)
        user = serializer.instance
        token, _ = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

class LoginView(generics.GenericAPIView):
    """
    API endpoint for user login.
    Returns a token upon successful login.
    """
    serializer_class = CustomUserSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(password):
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)