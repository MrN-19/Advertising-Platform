from django.contrib import admin
from . import models


class AdsCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(models.AdsCategory,AdsCategoryAdmin)

class AdsAdmin(admin.ModelAdmin):
    ...

admin.site.register(models.Ads,AdsAdmin)


