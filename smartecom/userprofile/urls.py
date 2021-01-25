from django.urls import path
from userprofile.views import (user_logout,user_login,
                               user_register,user_profile,user_update,user_password,usercomment,comment_delete)


urlpatterns=[
    path ('user_logout/',user_logout,name="user_logout"),
    path('user_login/',user_login,name='user_login'),
    path('user_register/',user_register,name="user_register"),
    path('user_profile/',user_profile,name="user_profile"),
    path('user_update/',user_update,name="user_update"),
    path('user_password/',user_password,name="user_password"),
    path('usercomment/',usercomment,name="usercomment"),
    path('comment_delete/<int:id>',comment_delete,name="comment_delete"),
]