
from django.contrib import admin
from django.urls import path,include
from flat import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve




urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("flat.urls")),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

