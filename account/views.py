from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny

from .serializers import UserRegisterSerializer,UserLoginSerializer
from tools.constant.messages.information_messages import SuccessfullMessages
from tools.constant.messages.error_messages import AuthenticationErrors
from ads.models import Ads,AdsPictures,AdsCategory,MarkedAds
from ads.serializers import AdsSerializer

class UserRegister(APIView):

    def post(self,request):

        user_register_serializer = UserRegisterSerializer(data = request.data)
        if user_register_serializer.is_valid():
            user = user_register_serializer.save()
            token:str = Token.objects.create(user = user).key
            return Response(data = {
                "message" : SuccessfullMessages.USER_REGISTER,
                "token" : token
            },status = status.HTTP_200_OK)
        return Response(data = user_register_serializer.error_messages,status = status.HTTP_400_BAD_REQUEST)
    
class UserLogin(APIView):

    def post(self,request):
        
        user_login_serializer = UserLoginSerializer(data = request.data)
        if user_login_serializer.is_valid():
            
            user = User.objects.filter(
                email = user_login_serializer.validated_data.get("email"),
            ).first()

            if user and check_password(user_login_serializer.validated_data.get("password"),user.password):
                token:str = Token.objects.get_or_create(user = user)[0].key
            else:
                return Response(data = {
                    "message" : AuthenticationErrors.INCORRECT_INFORMATION,
                },status=status.HTTP_400_BAD_REQUEST)

            return Response(data = {
                "message" : SuccessfullMessages.LOGIN_SUCCESSFULLY,
                "token" : token
            },status=status.HTTP_200_OK)
        return Response(data = user_login_serializer.error_messages,status = status.HTTP_400_BAD_REQUEST)
        
class UserMarkedAds(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request):
        
        marked_ads = MarkedAds.objects.filter(user = request.user).all()

        return Response(status=status.HTTP_200_OK)

class UserAds(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        
        user_ads = Ads.objects.filter(user = request.user).all()

        ads_serializer = AdsSerializer(instance = user_ads,many=True)

        return Response(data = ads_serializer.data,status=status.HTTP_200_OK)
    