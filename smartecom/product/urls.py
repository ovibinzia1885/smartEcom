from django.urls import path
from product.views import Comment_Add


urlpatterns=[
    path('Comment_Add/<int:id>/',Comment_Add,name="Comment_Add"),

]