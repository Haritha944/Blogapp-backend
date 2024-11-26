from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import RegisterSerializer,UserSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            refresh = RefreshToken.for_user(user)
            user_data = {
            'name': user.username,  # You can also use user.first_name if that's set
            'email': user.email,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'message': "User registered successfully"
        }

            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self,request):
        email=request.data.get("email")
        password=request.data.get("password")
        print(f"Attempting login with email: {email}, password: {password}")
        try:
            user=User.objects.get(email=email)
            if user.check_password(password):
                if user.is_active:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "message": "Login successful"
                    }, status=status.HTTP_200_OK)

                else:
                    return Response({"error": "Account is inactive."}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        


class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        user=request.user
        serializer = UserSerializer(user)
        print(serializer)
        return Response(serializer.data)