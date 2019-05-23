from django.urls import path
from .views import CreateUser, LoginView

urlpatterns = [
    path("auth/signup/", CreateUser.as_view(), name="user_signup"),
    path("auth/signin/", LoginView.as_view(), name="user_signin")
]