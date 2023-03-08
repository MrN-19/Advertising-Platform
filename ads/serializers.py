from rest_framework import serializers
from .models import Ads,AdsCategory


class AdsSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(source = "user.first_name")
    last_name = serializers.CharField(source = "user.last_name")

    class Meta:
        model = Ads
        fields = "__all__"