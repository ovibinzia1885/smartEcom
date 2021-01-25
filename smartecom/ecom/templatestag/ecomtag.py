from django import template
from ecom.models import Setting
from product.models import Category

register = template.Library()

@register.simple_tag
def ecom_cat():
    return Category.objects.all()

@register.simple_tag
def ecom_set():
    return Setting.objects.get(id=1)
