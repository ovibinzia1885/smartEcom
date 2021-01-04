from django.contrib import admin
from userprofile.models import USerprofile




class profileadmin(admin.ModelAdmin):
    model=USerprofile
    list_display = ['user','country','image_tag']
    list_filter = ['user']


admin.site.register(USerprofile,profileadmin)
