from rest_framework import viewsets, permissions, response
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination  # Add pagination class
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        # Optionally filter posts by user making the request
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.filter(author=user)
        return Post.objects.none()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class CommentViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination  # Add pagination class
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Get the post the comment is associated with
        post_id = self.request.data.get('post')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return response({'error': 'Invalid post ID provided.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        # Optionally filter comments by user making the request
        user = self.request.user
        if user.is_authenticated:
            return Comment.objects.filter(author=user)
        return Comment.objects.none()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    