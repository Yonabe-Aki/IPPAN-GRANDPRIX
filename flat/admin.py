from django.contrib import admin
from .models import Competition,Post,Tag,User
from social_django.models import UserSocialAuth


admin.site.register(Competition)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(User)


