from rest_framework import serializers

from .models import Ads,AdsCategory

from tools.constant.messages import error_messages


class AdsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AdsCategory
        fields = "__all__"

class AdsSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(source = "user.first_name")
    last_name = serializers.CharField(source = "user.last_name")
    
    city = serializers.CharField(source = "location.city")
    province = serializers.CharField(source = "location.province")
    
    category = serializers.CharField(source = "category.title")

    class Meta:
        model = Ads
        exclude = ("location","user")

class AddAdsSerializer(serializers.Serializer):

    def __init__(self, instance=None, data=..., **kwargs):
        
        self.__user = kwargs.get("user")
        
        super().__init__(instance, data, **kwargs)




    __PAYMENT_TYPE_CHOICES:tuple = (
        ("agreement","توافقی"),("fixed","مقطوع")
    )

    title = serializers.CharField(max_length = 200,error_messages = {
        "required" : error_messages.AdsTitle.REQUIRED_ERROR,
        "max_length" : error_messages.AdsTitle.MAX_LENGTH_ERROR
    })
    category = serializers.IntegerField(error_messages = {
        "required" : error_messages.CategoryTitle.REQUIRED_ERROR,
    })
    describtion = serializers.CharField(max_length = 1000,error_messages = {
        "required" : error_messages.Describtion.REQUIRED_ERROR,
        "max_length" : error_messages.Describtion.MAX_LENGTH_ERROR
    })
    payment_type = serializers.ChoiceField(choices=__PAYMENT_TYPE_CHOICES)
    price = serializers.IntegerField(default = 0,error_messages = {
        "required" : error_messages.Price.REQUIRED_ERROR,
    })
    images = serializers.ImageField()

    def validate_price(self,value:int):
        
        payment_type:str = self.validated_data.get("payment_type","")

        if value > 0 and payment_type == "agreement":
            raise serializers.ValidationError("if type is agreement , you should not enter price")
        return value
    
    def validate_category(self,value:int):
        if not value:
            raise serializers.ValidationError("Category Not Found ...")
        
        category = AdsCategory.objects.filter(id = value).exists()
        if not category:
            raise serializers.ValidationError("Category Not Found ...")
        
        return value
    
    def create(self, validated_data:dict):
        
        validated_data["user"] = self.__user
        validated_data["category"] = AdsCategory.objects.filter(id = validated_data.get("category",0)).first()
        return Ads(**validated_data)
    
    def update(self, instance, validated_data):

        category = AdsCategory.objects.filter(id = validated_data.get("category",0)).first()

        instance.title = validated_data.get("title")
        instance.user = self.__user
        instance.category = category
        instance.describtion = validated_data.get("describtion")
        instance.price = validated_data.price
        instance.payment_type = validated_data.get("payment_type")


