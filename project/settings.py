"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
import rest_framework_simplejwt
from dotenv import load_dotenv
dotenv_path = "./dotenv_files/.env"
load_dotenv(dotenv_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY","CHANGE_ME")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.getenv("DEBUG", 0)))

ALLOWED_HOSTS = [
    h.strip() for h in os.getenv("ALLOWED_HOSTS", "").split(",") if h.strip()
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ifoodApp',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'ifoodApp.middleware.JWTAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:8080",
    "https://frontendhifood-production.up.railway.app"
]

CORS_ALLOW_ALL_ORIGINS = bool(os.getenv('CORS_ALLOW_ALL_ORIGINS', False))

ROOT_URLCONF = 'project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_DRIVER',''),
        'NAME': os.getenv('PG_DB',''),
        'USER': os.getenv('PG_USER',''),
        'PASSWORD':os.getenv('POSTGRES_PASSWORD',''),
        'HOST': os.getenv('PG_HOST',''),
        'PORT': os.getenv('PG_PORT',''),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'ALGORITHM': os.getenv('JWT_ALGORITHM','CHANGE_ME'),
    'SIGNING_KEY': os.getenv('JWT_SECRET_KEY','CHANGE_ME'),
}
AUTHENTICATION_CLASSES = (
    'rest_framework_simplejwt.authentication.JWTAuthentication',
)
AUTH_USER_MODEL = 'ifoodApp.Usuario'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

DATA_DIR = BASE_DIR.parent / "data" / "web"

STATIC_URL = "/static/"
# /data/web/static
STATIC_ROOT = DATA_DIR / "static"

MEDIA_URL = "/media/"
# /data/web/media
MEDIA_ROOT = DATA_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
