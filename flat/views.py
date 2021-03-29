from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from .models import Competition,Tag
import json 
from requests_oauthlib import OAuth1Session
import ssl
from . import twitter_api
from . import create_img
import os
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist

ssl._create_default_https_context = ssl._create_unverified_context


def hold(request):
    user = request.user
    if user.is_authenticated:
        image_url=twitter_api.get_user_icon(request.user)
        return render(request,"flat/hold.html",{"image_url":image_url})
    else:
        return render(request,"flat/hold.html")


def detail(request,competition_id):
    competition=Competition.objects.get(id=competition_id)
    user = request.user
    if user.is_authenticated:
        image_url=twitter_api.get_user_icon(request.user)
        return render(request,"flat/detail.html",{"image_url":image_url,"competition":competition,"user":user})
    else:
        return render(request,"flat/detail.html",{"competition":competition,"user":user})


@login_required
def post(request,competition_id):
    if request.user.is_authenticated:
        competition = Competition.objects.get(id=competition_id)
        competition.population+=1
        competition.save()
        content=request.POST.get("content")
        twitter_api.post_twitter(request.user,content,competition_id)
        return redirect('/?flash=True')
    else:
        return redirect("/")

def create_competition(request):
    theme=request.POST.get("theme")
    new_competition=Competition(theme=theme)
    new_competition.save()
    id=new_competition.id
    create_img.create_img(theme,id)
    new_competition.img="img_"+str(id)+".jpg"
    new_competition.save()
    return redirect("/")


def paginate_queryset(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


def participate(request):
    competitions = Competition.objects.order_by("-id").all()
    page_obj = paginate_queryset(request, competitions, 5)
    user = request.user

    if user.is_authenticated:
        image_url=twitter_api.get_user_icon(request.user)
        try:
            if 'flash' in request.GET:
                flash_bool = request.GET['flash'] 
                context = {
                   'competition_list': page_obj.object_list,
                   'page_obj': page_obj,
                   "image_url" : image_url,  
                   "flash_bool": flash_bool,          
                }
                return render(request, 'flat/participate.html', context)
            else:
                context = {
                   'competition_list': page_obj.object_list,
                   'page_obj': page_obj,
                   "image_url" : image_url,                  
                }
                return render(request, 'flat/participate.html', context)
        except ObjectDoesNotExist:
            return redirect("logout")
    else:
        try:
            context = {
                'competition_list': page_obj.object_list,
                'page_obj': page_obj,
            }
            return render(request, "flat/participate.html", context)
        except ObjectDoesNotExist:
            return redirect("logout")


# def get_icon_url(request):
#     social_auth = UserSocialAuth.objects.get(user=request.user, provider='twitter')
#     screen_name=social_auth.extra_data["access_token"]["screen_name"]

#     if not os.path.exists(screen_name+'.jpg'):
#         twitter_api.get_user_icon(request.user)
#     return redirect("/")




