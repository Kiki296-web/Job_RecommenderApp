from django.urls import path
from . import views
from .views import RegisterView, LoginView, ProfileView,LogoutView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("me/", me, name="me"),
    
]
