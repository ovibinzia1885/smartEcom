from django.urls import path
from oderapp.views import Add_to_shoping_cart,cart_detials,cart_delete,OrderCart

urlpatterns=[
    path('addingcart/<int:id>/',Add_to_shoping_cart,name='Add_to_shoping_cart'),
    path('cart_details/',cart_detials,name="cart_details"),
    path('cart_delete/<int:id>/',cart_delete,name="cart_delete"),
    path('OrderCart/',OrderCart,name="OrderCart"),


]