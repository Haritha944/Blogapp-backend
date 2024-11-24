from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'id','username','email','phone_number',
            'profile_image','location','social_links','date_of_birth','is_active'
        ]
        extra_kwargs = {
            'email': {'required': True},
            'phone_number': {'required': True},
        }

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username','phone_number','password','profile_image','location']
        extra_kwags = {
            'password':{'write_only':True},
        }

    def create(self,validated_data):
        user=User(
            email=validated_data['email'],
            username=validated_data['username'],
            phone_number=validated_data.get('phone_number'),
            profile_image=validated_data.get('profile_image'),
            location=validated_data.get('location'),
            date_of_birth=validated_data.get('date_of_birth'),
        )
        user.set_password(validated_data['password'])
        print(f"Hashed password: {user.password}") 
        user.save()
        return user
                
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return value
        
    def validate_phone_number(Self,value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number consists of digits")
        if len(value)!=10:
            raise serializers.ValidationError("Phone number should be 10 digits")
        return value