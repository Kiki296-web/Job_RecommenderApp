from django.urls import path
from . import views
from .views import RegisterView, LoginView, ProfileView,LogoutView, me

urlpatterns = [
    # path('', views.user_list, name='user-list'), 
    # path('<int:id>/', views.user_detail, name='user-detail'),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("me/", me, name="me"),
    
]
