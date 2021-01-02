from django.urls import path
from .views import home,product_single,category_product,about,contact,SearchView

urlpatterns=[
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('contact/',contact,name="contact"),
    path('product_single/<int:id>/',product_single,name="product_single"),
    path('product_single/<int:id>/<slug:slug>/',category_product,name="category_product"),
    path('SearchView/',SearchView,name="SearchView"),


]