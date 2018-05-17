from .base import *
from django.urls import reverse_lazy

"""
Django settings for compiladores project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'compiladores',
        'USER': 'compiladores',
        'PASSWORD': 'compiladores',
        'HOST': 'localhost',
        'PORT': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
    'social_core.backends.twitter.TwitterOAuth', # for Twitter authetication
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='952278025126-vm7sd2ud0jmqafehbs7jvscn49qua1r2.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'OT_BTrCIk2A6kkrTvwOaCDdy'

SOCIAL_AUTH_GITHUB_KEY = '998d04fbf3c10b8236f5'
SOCIAL_AUTH_GITHUB_SECRET = '925a13611dc63355840581cbca94704c85d10b4a'

# CLIENTE DE OAUTH GOOGLE
# ID de cliente : 952278025126-vm7sd2ud0jmqafehbs7jvscn49qua1r2.apps.googleusercontent.com
# Secreto de cliente: OT_BTrCIk2A6kkrTvwOaCDdy

# CLIENTE DE OAUTH GITHUB
# ID de cliente : 998d04fbf3c10b8236f5
# Secreto de cliente: 925a13611dc63355840581cbca94704c85d10b4a

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/register' # Here goes the home where we are gonna work on