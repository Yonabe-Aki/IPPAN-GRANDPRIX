from django.db import models
from django.utils import timezone
from django.views.generic import TemplateView

class User(models.Model):
    name=models.CharField(max_length=50,default=0)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Post(models.Model):
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    user_id=models.IntegerField(default=0)
    competition_id=models.IntegerField(default=0)
    def __str__(self):
        return self.text
class Tag(models.Model):
    name=models.CharField(max_length=30,default=0)
    def __str__(self):
        return self.name
class Competition(models.Model):
    theme=models.CharField(max_length=50,default=0)
    img = models.ImageField(upload_to='', default='defo')
    population=models.IntegerField(default=0)
    def __str__(self):
        return self.theme
class TwitterPost(TemplateView):
    post_api = "https://api.twitter.com/1.1/statuses/update.json"

    def post(self, request, *args, **kwargs):
        social_user = UserSocialAuth.objects.filter(user=request.user).first()
        # ここでバリデーションを入れるべきでしょう。
        twitter_oauth = OAuth1Session(
            SOCIAL_AUTH_TWITTER_KEY,
            SOCIAL_AUTH_TWITTER_SECRET,
            social_user.tokens.get('oauth_token'),
            social_user.tokens.get('oauth_token_secret'),
        )
        params = {"status": 'twitter post api test.', "lang": "ja"}
        result = twitter_oauth.post(self.post_api, params)
        return redirect('home')


    






