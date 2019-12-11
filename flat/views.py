from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from .models import Competition,Tag
import json 
from requests_oauthlib import OAuth1Session
import ssl
from . import twitter_api
from . import create_img

ssl._create_default_https_context = ssl._create_unverified_context

def base(request):
    competitions=Competition.objects.all
    user=request.user
    return render(request,"flat/participate.html",{"competitions":competitions,"user":user})
def participate(request):
    user=request.user
    competitions=Competition.objects.all
    return render(request,"flat/participate.html",{"competitions":competitions,"user":user})
def hold(request):
    return render(request,"flat/hold.html")

def post(request,competition_id):
    content=request.POST.get("content")
    twitter_api.post_twitter(request.user,content,competition_id)
    return redirect("/")

def detail(request,competition_id):
    competition=Competition.objects.get(id=competition_id)
    return render(request,"flat/detail.html",{"competition":competition})

def create_competition(request):
    theme=request.POST.get("theme")
    id_tuple=Competition.objects.all().values_list('id', flat=True)
    if len(id_tuple)==0:
        id=1
    if len(id_tuple)!=0:
        id=id_tuple[len(id_tuple)-1]+1
    create_img.create_img(theme,id)
    new_competition=Competition(theme=theme,img="img_"+str(id)+".jpg")
    new_competition.save()
    return redirect("/")




