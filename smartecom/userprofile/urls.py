from django.urls import path
from userprofile.views import user_logout,user_login,user_register

urlpatterns=[
    path ('user_logout/',user_logout,name="user_logout"),
    path('user_login/',user_login,name='user_login'),
    path('user_register/',user_register,name="user_register"),
]