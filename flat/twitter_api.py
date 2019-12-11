from django.conf import settings
from social_django.models import UserSocialAuth
from requests_oauthlib import OAuth1Session
import twitter
import json
import sys
sys.path.append("../mysite")
from mysite import settings
def post_twitter(user,content,competition_id):
    social_auth = UserSocialAuth.objects.get(user=user, provider='twitter')

    CK = settings.SOCIAL_AUTH_TWITTER_KEY                         
    CS = settings.SOCIAL_AUTH_TWITTER_SECRET    
    AT = social_auth.extra_data['access_token']['oauth_token']
    AS = social_auth.extra_data['access_token']['oauth_token_secret']

    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"
    attachment_url="http://127.0.0.1:8000/"

    twitter = OAuth1Session(CK, CS, AT, AS)



    params = {'status': content+"\nhttps://omusubi.herokuapp.com/detail/"+str(competition_id)}
    req_media = twitter.post(url_text, params = params)

    