from django.urls import path

from .views import UserRegister

app_name:str = "account"

urlpatterns = [
    path("register",UserRegister.as_view(),name="register"),
]
