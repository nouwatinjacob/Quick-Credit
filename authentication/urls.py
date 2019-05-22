from django.urls import path
from .views import CreateUser

urlpatterns = [
    path("auth/signup/", CreateUser.as_view(), name="user_create"),
]