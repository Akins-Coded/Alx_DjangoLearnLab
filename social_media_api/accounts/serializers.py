from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        token, _ = Token.objects.create(user=user)
        validated_data['token'] = token.key
        return user

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'bio', 'profile_picture', 'password', 'token', 'followers', 'following')
        read_only_fields = ('followers', 'following')
       