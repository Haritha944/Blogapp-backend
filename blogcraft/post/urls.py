from django.urls import path
from .views import BlogPostAPI,BlogDetail,BlogCollection


urlpatterns=[
    path('posts/', BlogPostAPI.as_view(), name='blogpost-list'),
    path('blog/<int:id>/', BlogDetail.as_view(), name='blog-detail'),
    path('blogsview/', BlogCollection.as_view(), name='blog-collect'),
]