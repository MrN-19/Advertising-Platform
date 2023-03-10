from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser

from .models import Ads,AdsCategory
from .serializers import AdsSerializer,AdsCategorySerializer,AddAdsSerializer


class AllCategories(APIView):

    def get(self,request):

        all_categories = AdsCategory.objects.all()

        ads_category_serializer = AdsCategorySerializer(instance = all_categories,many=True)

        return Response(data = ads_category_serializer.data,status=status.HTTP_200_OK)       

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
    
class AllAds(APIView):

    def get(self,request):

        all_ads = Ads.objects.order_by("-publish_date").all()

        all_ads_serializer = AdsSerializer(instance = all_ads,many=True)
        return Response(data = all_ads_serializer.data,status=status.HTTP_200_OK)
    
class AdsByCityProvince(APIView):

    def get(self,request,city_province:str):

        if not city_province:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        ads_by_city = Ads.objects.filter(Q(location__city = city_province) | Q(location__province = city_province)).order_by("-publish_date").all()

        ads_by_city_serializer = AdsSerializer(instance=ads_by_city,many=True)
        return Response(data = ads_by_city_serializer.data,status=status.HTTP_200_OK)
    
class NewAds(APIView):

    # permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    def post(self,request):
        
        new_ads_serializer = AddAdsSerializer(data = request.data)
        if new_ads_serializer.is_valid():
            new_ads_serializer.save()

        return Response(status=status.HTTP_200_OK)




        
