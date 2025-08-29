from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.views import View
from .forms import CustomUserCreationForm  

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "users/register.html", {"form": form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # log them in immediately
            return redirect("profile")   # redirect to profile after registration
        return render(request, "users/register.html", {"form": form})

# Login (returns token)
class LoginView(View):
    def get(self, request):
        # Show a simple login form in the browser
        return render(request, "users/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect("profile")   # after successful login, go to profile
        else:
            return render(request, "users/login.html", {
                "error": "Invalid username or password"
            })

# Profile (requires authentication)
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


