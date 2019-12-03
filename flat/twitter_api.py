from django.conf import settings
from social_django.models import UserSocialAuth
from requests_oauthlib import OAuth1Session

import twitter
import json
def post_twitter(user):
    social_auth = UserSocialAuth.objects.get(user=user, provider='twitter')

    CK = 'ctGFBxVyAK5hHYmF5weDduyCa'                             # 
    CS = 'GjRAFSFBjCBvSYOx7cXXwtnpmDYyp8u8GQi0nGIskbPEIO2mBR'         
    AT = social_auth.extra_data['access_token']['oauth_token']
    AS = social_auth.extra_data['access_token']['oauth_token_secret']

    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"
    attachment_url="http://127.0.0.1:8000/"
    # OAuth認証 セッションを開始
    twitter = OAuth1Session(CK, CS, AT, AS)


    # Media ID を付加してテキストを投稿
    params = {'status': '画像投稿テスト http://127.0.0.1:8000/'}
    req_media = twitter.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_media.status_code != 200:
        print ("テキストアップデート失敗: %s", req_text.text)
        exit()

    print ("OK")
