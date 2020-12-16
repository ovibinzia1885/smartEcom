from django.shortcuts import render
from ecom.models import Setting
from product.models import Product

def home(request):
    setting=Setting.objects.get(id=1)
    slide_img=Product.objects.all().order_by('id')[:2]
    lasted_product=Product.objects.all().order_by('-id')
    context={'setting':setting,'slide_img':slide_img,'lasted_product':lasted_product}
    return render(request,'home.html',context)
