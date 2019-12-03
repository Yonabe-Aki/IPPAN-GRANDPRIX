from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from .models import Competition,Tag
import json 
from requests_oauthlib import OAuth1Session
import ssl
from . import twitter_api

ssl._create_default_https_context = ssl._create_unverified_context

@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    return render(request,'flat/top.html',{'user': user})

def base(request):
    competitions=Competition.objects.all
    return render(request,"flat/participate.html",{"competitions":competitions})
def participate(request):
    user=request.user
    competitions=Competition.objects.all
    return render(request,"flat/participate.html",{"competitions":competitions,"user":user})
def hold(request):
    return render(request,"flat/hold.html")
def acount(request):
    return render(request,"flat/acount.html")

def post(request):
    twitter_api.post_twitter(request.user)
    return redirect("/")


