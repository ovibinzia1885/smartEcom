from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class USerprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    phonenumber=models.CharField(max_length=20)
    adderess=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=150,blank=True)
    country=models.CharField(max_length=150,blank=True)
    image=models.ImageField(upload_to='user_img')

    def  __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + '[' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" heights="50" width="50" />'.format(self.image.url))

    image_tag.short_description = 'Image'


