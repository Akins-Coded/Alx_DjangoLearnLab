from posts.models import Post, Like
from .models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

User = get_user_model()

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(recipient=user).order_by('-timestamp')

    @action(detail=False, methods=['post'])
    def like_post(self, request):
        # Get the user and post from the request data
        user = request.user
        post_id = request.data.get('post_id')  # Assuming post_id is passed
        post = Post.objects.get(id=post_id)  # Handle exception if post not found

        # Create the Like
        like = Like.objects.create(user=user, post=post)

        # Create the notification for the post's author
        actor = user
        recipient = post.author
        verb = "liked your post"

        # Create the ContentType for Post
        content_type = ContentType.objects.get_for_model(Post)

        # Create the notification
        notification = Notification.objects.create(
            recipient=recipient,
            actor=actor,
            verb=verb,
            target_content_type=content_type,
            target_object_id=post.id
        )

        # Return the notification response
        return Response({
            "message": "Notification created successfully",
            "notification": {
                "recipient": notification.recipient.username,
                "actor": notification.actor.username,
                "verb": notification.verb,
                "timestamp": notification.timestamp,
            }
        })
