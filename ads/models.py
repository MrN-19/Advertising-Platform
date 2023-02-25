from django.db import models
from django.contrib.auth.models import User

class AdsCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="عنوان دسته بندی")
    header = models.ForeignKey("self",on_delete=models.CASCADE,verbose_name="سر گروه",null=True,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "دسته بندی آگهی ها"


class Ads(models.Model):

    PAYMENT_CHOICES = (("agreement","توافقی"),("fixed","مقطوع"))

    title = models.CharField(max_length=200,verbose_name="عنوان آگهی")
    category = models.ForeignKey(AdsCategory,on_delete=models.CASCADE,verbose_name="دسته بندی",related_name="ads")
    describtion = models.TextField(max_length=1000,verbose_name="توضیحات آگهی")
    payment_type = models.CharField(max_length=120,choices=PAYMENT_CHOICES,verbose_name="نوع پرداخت")
    price = models.PositiveBigIntegerField(verbose_name="مبلغ",null=True,blank=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "آگهی ها"

class AdsPictures(models.Model):
    ads = models.ForeignKey(Ads,on_delete=models.CASCADE,null=True)
    picture = models.ImageField(upload_to="Ads/AdsPictures/",verbose_name="تصویر آگهی")

    def __str__(self):
        return self.ads.title
    
    class Meta:
        verbose_name_plural = "تصاویر آگهی "

