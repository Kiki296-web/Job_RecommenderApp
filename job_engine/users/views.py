# users/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
from django.shortcuts import redirect
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


# Regsiter Page
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User has been registered successfully",
                "token": token.key,
                "username": user.username
            })
        return Response(serializer.errors, status=400)


#Login Page
class LoginView(View):
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({"detail": "Send POST request with username & password", "csrf_token": csrf_token})

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return redirect("profile")  # redirect after login
        return JsonResponse({"error": "Invalid credentials"}, status=400)


# Profile page
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


#Logout Page
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
