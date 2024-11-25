from django.db import models
from account.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title