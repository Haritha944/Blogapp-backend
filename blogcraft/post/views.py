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
        blog_posts = Post.objects.filter(user=request.user)
        
        if not blog_posts.exists():
            return Response({"detail": "No posts found for this user."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(blog_posts, many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serilaizer=PostSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save(user=request.user)
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetail(APIView):
    permission_classes=[IsAuthenticated]
    def put(self,request,id):
        try:
            post=Post.objects.get(id=id)
        except Post.DoesNotExist:
            return Response({"Post is not existed"},status=status.HTTP_404_NOT_FOUND)
        #user=post.user 
        serializer=PostSerializer(post,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


