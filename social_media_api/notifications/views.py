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
    def like_post(self, request, *args, **kwargs):
        # Get the post using the post_id passed in the request
        pk = request.data.get('post_id')  # Assuming post_id is passed
        post = Post.objects.get(id=pk)  # Handle exception if post not found

        # Create or retrieve the Like for the user and post
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({
                "message": "You have already liked this post."
            }, status=400)

        # Create the notification for the post's author
        actor = request.user
        recipient = post.author
        verb = "liked your post"

        # Create the ContentType for Post
        content_type = ContentType.objects.get_for_model(Post)

        # Check if a notification already exists for this like
        notification_exists = Notification.objects.filter(
            recipient=recipient,
            actor=actor,
            verb=verb,
            target_content_type=content_type,
            target_object_id=post.id
        ).exists()

        if not notification_exists:
            # Create the notification if it does not exist
            Notification.objects.create(
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
                "recipient": recipient.username,
                "actor": actor.username,
                "verb": verb,
                "timestamp": Notification.objects.filter(recipient=recipient).latest('timestamp').timestamp,
            }
        })
