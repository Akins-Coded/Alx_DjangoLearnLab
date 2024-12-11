from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import CustomUserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    class Meta:
        model = Post
        feilds = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    class Meta:
        model = Comment
        feilds = '__all__'

