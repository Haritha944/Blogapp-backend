from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post

class BlogPostAPI(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self,request):
        blog_posts = Post.objects.all()
        serializer = PostSerializer(blog_posts, many=True)
        return Response(serializer.data)
    def post(self,request):
        serilaizer=PostSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save(user=request.user)
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

