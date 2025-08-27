# users/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ProfileView, me

urlpatterns = [
    path('', views.user_list, name='user-list'),  # handles GET /api/users/
    path('<int:id>/', views.user_detail, name='user-detail'),  # handles /api/users/1/
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("me/", me, name="me"),
]
