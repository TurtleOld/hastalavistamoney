"""
Django settings for hasta_la_vista_money project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

import dj_database_url
import rollbar
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'true').lower() in {'yes', '1', 'true'}

ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
).split(',') if os.environ.get(
    'ALLOWED_HOSTS',
) else ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'locale',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_bootstrap5',
    'hasta_la_vista_money.bot',
    'hasta_la_vista_money',
    'hasta_la_vista_money.applications',
    'hasta_la_vista_money.expense',
    'hasta_la_vista_money.income',
    'hasta_la_vista_money.receipts',
    'hasta_la_vista_money.users',
]

AUTH_USER_MODEL = 'users.User'

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'csp.middleware.CSPMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]
#
# CSP_DEFAULT_SRC = (
#     "'self'",
#     'https://money.pavlovteam.ru',
#     'https://api.telegram.org',
# )
# CSP_SCRIPT_SRC = (
#     "'self'",
#     "'unsafe-inline'",
#     'https://cdn.jsdelivr.net',
#     'https://code.jquery.com',
#     'https://money.pavlovteam.ru',
#     'https://api.telegram.org',
# )
# CSP_STYLE_SRC = (
#     "'self'",
#     "'unsafe-inline'",
#     'https://cdn.jsdelivr.net',
#     'https://money.pavlovteam.ru',
# )
# CSP_IMG_SRC = ("'self'", 'data:', 'https://money.pavlovteam.ru')
# CSP_FONT_SRC = ("'self'", 'https://money.pavlovteam.ru')
# CSP_CONNECT_SRC = ("'self'", 'https://api.telegram.org')
# CSP_FRAME_SRC = ("'self'",)
# CSP_BASE_URI = ("'none'",)
# CSP_OBJECT_SRC = ("'none'",)

ROOT_URLCONF = 'hasta_la_vista_money.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hasta_la_vista_money.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend'
    ),
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}

if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },
    }

CONN_MAX_AGE = 500

if os.getenv('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(conn_max_age=CONN_MAX_AGE)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = False

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = os.path.join(BASE_DIR, 'static/')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if os.environ.get('ACCESS_TOKEN') is not None:
    ROLLBAR = {
        'access_token': os.environ.get('ACCESS_TOKEN'),
        'environment': 'development' if DEBUG else 'production',
        'patch_debugview': False,
        'root': BASE_DIR,
    }

    rollbar.init(**ROLLBAR)
