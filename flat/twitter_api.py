from django.conf import settings
from social_django.models import UserSocialAuth
from requests_oauthlib import OAuth1Session
import twitter
import json
import sys
import requests

sys.path.append("../mysite")
from mysite import settings
def post_twitter(user,content,competition_id):

    social_auth = UserSocialAuth.objects.get(user=user, provider='twitter')

    CK = settings.SOCIAL_AUTH_TWITTER_KEY                         
    CS = settings.SOCIAL_AUTH_TWITTER_SECRET    
    AT = social_auth.extra_data['access_token']['oauth_token']
    AS = social_auth.extra_data['access_token']['oauth_token_secret']

    url_text = "https://api.twitter.com/1.1/statuses/update.json"
    twitter = OAuth1Session(CK, CS, AT, AS)
    params = {'status': content+"\nhttps://omusubi.herokuapp.com/detail/"+str(competition_id)}
    twitter.post(url_text, params = params)

def get_user_icon(user):

    social_auth = UserSocialAuth.objects.get(user=user, provider='twitter')

    CK = settings.SOCIAL_AUTH_TWITTER_KEY                         
    CS = settings.SOCIAL_AUTH_TWITTER_SECRET    
    AT = social_auth.extra_data['access_token']['oauth_token']
    AS = social_auth.extra_data['access_token']['oauth_token_secret']
    screen_name=social_auth.extra_data["access_token"]["screen_name"]

    url_text="https://api.twitter.com/1.1/users/show.json"
    twitter = OAuth1Session(CK, CS, AT, AS)
    params = {"screen_name":screen_name,"include_entities":False}

    res=twitter.get(url_text,params=params).json()
    url=res["profile_image_url"]
    print(url)

    file_name = "media/"+screen_name+".jpg"

    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as aaa:
        aaa.write(image)





    