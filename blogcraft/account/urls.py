from django.urls import path
from .views import RegisterView,LoginView,UserProfileView

urlpatterns=[
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='register'),
    path('user/details/', UserProfileView.as_view(), name='user-details'),
]