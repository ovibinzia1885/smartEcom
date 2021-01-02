from django.contrib import admin
from oderapp.models import ShopCart



class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['product','user','quantity','price','amount']
    list_filter = ['user']




admin.site.register(ShopCart,ShopcartAdmin)