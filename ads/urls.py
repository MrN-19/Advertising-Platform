from django.urls import path
from .views import AdsByCategory

app_name:str = "ads"

urlpatterns = [
    path("category/<str:slug>",AdsByCategory.as_view(),name="adsbycategory"),
]