from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
# Assuming `user` is the current user, and `post` is the post being liked
User = get_user_model()
# Create a like
like = Like.objects.create(user=user, post=post)

# Create a notification for the post's author
actor = User
recipient = Post.author
verb = "liked your post"

# Create the ContentType for Post
content_type = ContentType.objects.get_for_model(Post)

# Create the notification
notification = Notification.objects.create(
    recipient=recipient,
    actor=actor,
    verb=verb,
    target_content_type=content_type,
    target_object_id=Post.id
)