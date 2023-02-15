from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegisterSerializer
from tools.constant.messages.information_messages import SuccessfullMessages

class UserRegister(APIView):

    def post(self,request):

        user_register_serializer = UserRegisterSerializer(request.data)
        if user_register_serializer.is_valide():
            user_register_serializer.save()
            return Response(data = {
                "message" : SuccessfullMessages.USER_REGISTER,
            },status = status.HTTP_200_OK)
        return Response(data = user_register_serializer.error_messages,status = status.HTTP_400_BADREQUEST)
