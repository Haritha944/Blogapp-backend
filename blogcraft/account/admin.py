from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone_number', 'is_staff', 'is_active')
    search_fields = ('email', 'username', 'phone_number')
    ordering = ('email',)