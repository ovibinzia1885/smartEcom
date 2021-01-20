from django.urls import path
from oderapp.views import Add_to_shoping_cart,cart_detials,cart_delete,OrderCart,Oder_showing,Order_Product_showing

urlpatterns=[
    path('addingcart/<int:id>/',Add_to_shoping_cart,name='Add_to_shoping_cart'),
    path('cart_details/',cart_detials,name="cart_details"),
    path('cart_delete/<int:id>/',cart_delete,name="cart_delete"),
    path('OrderCart/',OrderCart,name="OrderCart"),
    path('Oder_showing/',Oder_showing,name="Oder_showing"),
    path('Order_Product_showing/',Order_Product_showing,name="Order_Product_showing"),


]