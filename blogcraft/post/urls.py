from django.urls import path
from .views import BlogPostAPI


urlpatterns=[
    path('posts/', BlogPostAPI.as_view(), name='blogpost-list'),
]