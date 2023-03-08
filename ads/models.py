from django.db import models
from django.contrib.auth.models import User

class AdsCategory(models.Model):
    title = models.CharField(max_length=150,verbose_name="عنوان دسته بندی")
    header = models.ForeignKey("self",on_delete=models.CASCADE,verbose_name="سر گروه",null=True,blank=True)
    slug = models.SlugField(allow_unicode = True,unique=True,max_length=200,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "دسته بندی آگهی ها"


class Ads(models.Model):

    PAYMENT_CHOICES = (("agreement","توافقی"),("fixed","مقطوع"))
    
    title = models.CharField(max_length=200,verbose_name="عنوان آگهی")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر",null=True)
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

class MarkedAds(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    ads = models.ForeignKey(Ads,on_delete=models.CASCADE,verbose_name="آگهی")

    def __str__(self):
        return self.user.username + " " + self.ads.title
    
    class Meta:
        verbose_name_plural = "آگهی های برچسب شده"