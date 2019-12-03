
import django.contrib.auth.views
from django.urls import path,include
from django.conf.urls import url
from . import views
from .models import TwitterPost
app_name="flat"

urlpatterns=[
    path("hold",views.hold,name="hold"),
    path("",views.participate,name="participate"),
    path("acount",views.acount,name="acount"),
    path('top/',views.top_page, name="top"), 
    path("post",views.post,name="post",)
]



