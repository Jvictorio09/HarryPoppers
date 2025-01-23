"""
Django settings for myProject project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

PORT = os.getenv('PORT', '8080')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3m_11*ys32an(v87@yy0h#v0$2ac8r6$@=orgb50m6#hvoiowh"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    'harrypoppers-production.up.railway.app',
    '127.0.0.1',  # If you also want to allow local development
    'localhost',
    'https://www.harrypoppers.net/',
    'www.harrypoppers.net',
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myApp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ROOT_URLCONF = "myProject.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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



WSGI_APPLICATION = "myProject.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For collected static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'myApp', 'static', 'assets')]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# settings.py

MEDIA_URL = '/media/'  # The URL path for uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'myApp/static/assets/img/updated_images')  # Upload folder path

import os
import environ

# Initialize django-environ
env = environ.Env()

# Load environment variables from .env file (if exists)
environ.Env.read_env()

# Function to fetch environment variables with fallback to os.getenv
def get_env(var_name, default=None):
    """
    Fetch environment variable using django-environ first,
    then fallback to os.getenv if not found.
    """
    return env(var_name, default=os.getenv(var_name, default))

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'harrypopperstore@gmail.com'
EMAIL_HOST_PASSWORD = 'utpq mydr ngep sodu'  # App Password without spaces
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


'''           
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = int(get_env('EMAIL_PORT', default=587))
EMAIL_USE_TLS = get_env('EMAIL_USE_TLS', default=True) in [True, 'True', 'true', 1, '1']
EMAIL_HOST_USER = get_env('EMAIL_HOST_USER', default='harrypopperstore@gmail.com')
EMAIL_HOST_PASSWORD = get_env('EMAIL_HOST_PASSWORD')  # App password
DEFAULT_FROM_EMAIL = get_env('DEFAULT_FROM_EMAIL', default=EMAIL_HOST_USER)
'''