from django.urls import path
from .views import AdsByCategory,AllAds,AdsByCityProvince,AllCategories,NewAds

app_name:str = "ads"

urlpatterns = [
    path("",AllAds.as_view(),name="allads"),
    path("categories",AllCategories.as_view(),name="allcategories"),
    path("category/<str:slug>",AdsByCategory.as_view(),name="adsbycategory"),
    path("<str:city_province>",AdsByCityProvince.as_view(),name="adsbycity"),
    path("new/",NewAds.as_view(),name="newads"),
]