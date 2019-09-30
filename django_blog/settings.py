"""
Django settings for django_blog project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from config import *
from dotenv import load_dotenv
load_dotenv()
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# print(os.getenv())
SECRET_KEY = os.getenv("SECRET_KEY")
# print(type(SECRET_KEY))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_mfa',
    'blogpost',
    # 'social_django',
    # 'social.apps.django_app.default',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social.apps.django_app.context_processors.backends',
    # 'social.apps.django_app.context_processors.login_redirect',


    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.core.context_processors.static',
#     'django.core.context_processors.tz',
#     'django.contrib.messages.context_processors.messages',
#     'social.apps.django_app.context_processors.backends',
#     'social.apps.django_app.context_processors.login_redirect',
# )

ROOT_URLCONF = 'django_blog.urls'

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

                # 'social_django.context_processors.backends',  # <--
                # 'social_django.context_processors.login_redirect',
            ],
        },
    },
]

# AUTHENTICATION_BACKENDS = (
#     # 'social.backends.facebook.FacebookOAuth2',
#     # 'social.backends.google.GoogleOAuth2',
#     'social.backends.twitter.TwitterOAuth',
#     'django.contrib.auth.backends.ModelBackend',
# )

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_blog1',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'MEDIA')

MEDIA_URL = '/media/'



# SOCIAL_AUTH_TWITTER_KEY = '783730485784551424-qVTj0jmugqIRd6YANv1NZwXqm0DbyTd'
# SOCIAL_AUTH_TWITTER_SECRET = '2PCFkaBu1ovjObPuVOSs9pNj3hlWGlmG22P1oWKdIhShS '
#
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/register/'
# SOCIAL_AUTH_LOGIN_URL = '/login/'

# SOCIAL_AUTH_TWITTER_KEY = 'update me'
# SOCIAL_AUTH_TWITTER_SECRET = 'update me'
# SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False
# SOCIAL_AUTH_GITHUB_KEY = '13599985263541e9dcc9'
# SOCIAL_AUTH_GITHUB_SECRET = '76e0726ab5698d8f62cc6833f428b71689428c3d'
