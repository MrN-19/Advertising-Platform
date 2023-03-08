from django.urls import path

from .views import UserRegister,UserLogin,UserMarkedAds

app_name:str = "account"

urlpatterns = [
    path("register",UserRegister.as_view(),name="register"),
    path("login",UserLogin.as_view(),name="login"),
    path("marked-ads",UserMarkedAds.as_view(),name="markedads"),
]
