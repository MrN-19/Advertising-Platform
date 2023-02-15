from django.contrib.auth.models import User

from rest_framework import serializers

from tools.constant.messages.error_messages import EmailErrors,PasswordErrors,RePasswordErrors

class UserAuthenticationSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length = 150,error_messages = {
        "required" : EmailErrors.EMAIL_MAX_LENGTH,
        "max_length" : EmailErrors.EMAIL_MIN_LENGTH,
        "blank" : EmailErrors.EMAIL_MAX_LENGTH,
    })
    password = serializers.CharField(max_length = 100,min_length = 10,error_messages = {
        "required" : PasswordErrors.PASSWORD_REQUIRED,
        "max_length" : PasswordErrors.PASSWORD_MAX_LENGTH,
        "min_length" : PasswordErrors.PASSWORD_MIN_LENGTH,
    })

class UserRegisterSerializer(UserAuthenticationSerializer):

    re_password = serializers.CharField(max_length = 100,min_length = 10,error_messages = {
        "required" : PasswordErrors.PASSWORD_REQUIRED,
        "max_length" : PasswordErrors.PASSWORD_MAX_LENGTH,
        "min_length" : PasswordErrors.PASSWORD_MIN_LENGTH,
    })

    def validate_re_password(self):
        password:str = self.validated_data.get("password")
        re_password:str = self.validated_data.get("re_password")

        if password != re_password:
            raise serializers.ValidationError(RePasswordErrors.NOT_SAME)
        return re_password

    def create(self,validated_data):
        email:str = validated_data.get("email")
        password:str = validated_data.get("password")

        self.__user = User(
            username = email,
            email = email,
        )
        self.__user.set_password(password)
        self.__user.save()

    @property
    def user(self):
        return self.__user


class UserLoginSerializer(UserAuthenticationSerializer):
    ...
