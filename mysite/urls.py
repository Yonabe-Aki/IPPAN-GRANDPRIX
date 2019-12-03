
from django.contrib import admin
from django.urls import path,include
from flat import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("flat.urls")),
    path('', include('social_django.urls', namespace='social')),
]

