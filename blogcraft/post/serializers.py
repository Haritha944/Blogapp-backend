# serializers.py
from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'image','user','created_at', 'updated_at']
