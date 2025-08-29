from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


# Register new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# Login (returns token)
class LoginView(ObtainAuthToken):
    def get(self, request, *args, **kwargs):
        # Show login form in browser
        return render(request, "users/login.html")

    def post(self, request, *args, **kwargs):
        # If the request is coming from the HTML form
        if "username" in request.POST and "password" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Create or get token
                token, _ = Token.objects.get_or_create(user=user)
                # Redirect to profile page
                return redirect("/api/users/profile/")
            else:
                return render(request, "users/login.html", {"error": "Invalid credentials"})

        # Otherwise, fall back to API token login (for Postman etc.)
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response(
            {
                "token": token.key,
                "user_id": token.user_id,
                "username": token.user.username,
            },
            status=status.HTTP_200_OK,
        )

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


