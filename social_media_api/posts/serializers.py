from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        feilds = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        feilds = '__all__'

