from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .serializers import RegisterSerializer, UserSerializer
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomRegisterForm
from django.urls import reverse_lazy
from django.views.generic import FormView

class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = CustomRegisterForm
    success_url = reverse_lazy("profile")  # redirect after success

    def form_valid(self, form):
        user = form.save()
        # automatically log the user in after registering
        login(self.request, user)
        return super().form_valid(form)

# Login (returns token)
class LoginView(View):
    def get(self, request):
        # Shows a simple login form in the browser
        return render(request, "users/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect("profile")   # after successful login, it will go to profile
        else:
            return render(request, "users/login.html", {
                "error": "Invalid username or password"
            })

class ProfileView(LoginRequiredMixin, View):
    login_url = "login"   # if not logged in, it will redirect here

    def get(self, request):
        return render(request, "users/profile.html", {
            "user": request.user
        })
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")

    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


