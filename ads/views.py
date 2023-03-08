from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Ads,AdsCategory
from .serializers import AdsSerializer

class AdsByCategory(APIView):

    def get(self,request,slug:str):
        
        if not slug:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        category = AdsCategory.objects.filter(slug = slug).first()

        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND) 

        ads_by_category = Ads.objects.filter(category = category).all()
        
        ads_by_category_serializer = AdsSerializer(instance = ads_by_category,many=True)

        return Response(data = ads_by_category_serializer.data,status=status.HTTP_200_OK)
