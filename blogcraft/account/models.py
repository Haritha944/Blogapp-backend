from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=11,null=True,unique=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    location=models.CharField(max_length=255,null=True,blank=True)
    social_links = models.JSONField(blank=True, null=True, help_text="Store social media links as JSON")
    date_of_birth=models.DateField(blank=True,null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username', 'phone_number'] 
    def __str__(self):
        return self.email
