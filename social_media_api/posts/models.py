from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, max_length=50, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated__at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}, Posted {self.content}"
    
class Comment(models.Model):
    author = models.ForeignKey(User, max_length=50, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, max_length=50, related_name='post', on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated__at = models.DateTimeField(auto_now_add=True)


