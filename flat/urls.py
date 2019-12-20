
import django.contrib.auth.views
from django.urls import path,include
from django.conf.urls import url
from . import views
from .models import TwitterPost
app_name="flat"

urlpatterns=[
    path("hold",views.hold,name="hold"),
    path("",views.participate,name="participate"),
    path("post/<int:competition_id>",views.post,name="post"),
    path("detail/<int:competition_id>",views.detail,name="detail"),

    path("create/competition",views.create_competition,name="create_competition"),
    # path("create/image",views.get_icon_url),
]






