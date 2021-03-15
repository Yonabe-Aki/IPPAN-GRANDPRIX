"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
# mode="ローカルテスト"
# mode="ローカルテスト2"
# mode="テスト"
mode="本番"

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "flat",
    "social_django",
    "storages",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
LOGIN_REDIRECT_URL = "/"
LOGIN_URL="/login/twitter"
LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_TWITTER_AUTH_EXTRA_ARGUMENTS = {"force_login":"true"}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)



SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/' 
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



if mode=="ローカルテスト":
    DEBUG=True
    from .configs import twitter
    SECRET_KEY = twitter.SECRET_KEY
    SOCIAL_AUTH_TWITTER_KEY = twitter.SOCIAL_AUTH_TWITTER_KEY
    SOCIAL_AUTH_TWITTER_SECRET = twitter.SOCIAL_AUTH_TWITTER_SECRET
    AWS_ACCESS_KEY_ID=twitter.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY=twitter.AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME=twitter.AWS_STORAGE_BUCKET_NAME

if mode=="ローカルテスト2":
    DEBUG=False
    from .configs import twitter
    SECRET_KEY = twitter.SECRET_KEY
    SOCIAL_AUTH_TWITTER_KEY = twitter.SOCIAL_AUTH_TWITTER_KEY
    SOCIAL_AUTH_TWITTER_SECRET = twitter.SOCIAL_AUTH_TWITTER_SECRET
    AWS_ACCESS_KEY_ID=twitter.AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY=twitter.AWS_SECRET_ACCESS_KEY
    AWS_STORAGE_BUCKET_NAME=twitter.AWS_STORAGE_BUCKET_NAME


if mode=="テスト":
    DEBUG=True
    try:
        from .local_settings import *
    except ImportError:
        pass
    import django_heroku
    django_heroku.settings(locals())

    SECRET_KEY = os.environ["SECRET_KEY"]
    SOCIAL_AUTH_TWITTER_KEY = os.environ["SOCIAL_AUTH_TWITTER_KEY"]
    SOCIAL_AUTH_TWITTER_SECRET = os.environ["SOCIAL_AUTH_TWITTER_SECRET"]
    AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME=os.environ['AWS_STORAGE_BUCKET_NAME']

if mode=="本番":
    DEBUG=False
    TEMPLATE_DEBUG=True
    SECRET_KEY = os.environ["SECRET_KEY"]
    SOCIAL_AUTH_TWITTER_KEY = os.environ["SOCIAL_AUTH_TWITTER_KEY"]
    SOCIAL_AUTH_TWITTER_SECRET = os.environ["SOCIAL_AUTH_TWITTER_SECRET"]
    AWS_ACCESS_KEY_ID=os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME=os.environ['AWS_STORAGE_BUCKET_NAME']

        
    import dj_database_url

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'name',
            'USER': 'user',
            'PASSWORD': '',
            'HOST': 'host',
            'PORT': '',
        }
    }

    db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
    DATABASES['default'].update(db_from_env)    
    django_heroku.settings(locals()) #追加
    

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400', 
}

AWS_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
