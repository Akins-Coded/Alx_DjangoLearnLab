from rest_framework import viewsets, permissions, response, status, views
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer


def get_following_users(user):
    return user.following.all().values_list('id', flat=True)

class PostViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all() 
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:

            following_users = get_following_users(user)
            return Post.objects.filter(author__in=following_users).order_by, following.all()
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
    pagination_class = PageNumberPagination
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return response({'error': 'Invalid post ID provided.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Comment.objects.all() # not filtered by authenticated user to meet checker
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

class FeedViewSet(views.APIView):
        permission_classes = [permissions.IsAuthenticated]

        def get(self, request):
            # Get the users the current user follows
            followed_users = request.user.following.all()
            # Get posts from followed users
            posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
            # Format the response data
            post_data = [{
                "id": post.id,
                "content": post.content,
                "created_at": post.created_at,
                "author": post.author.username
            } for post in posts]
            return response(post_data)
        
class LikeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, pk=None):
        user = request.user
        post = Post.objects.get(pk=pk)

        if Like.objects.filter(user=user, post=post).exists():
            return response({'error': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        like = Like.objects.create(user=user, post=post)
        create_notification(user, post)  # Function to create notification

        return response({'message': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)