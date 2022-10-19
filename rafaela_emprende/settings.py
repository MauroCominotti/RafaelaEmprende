"""
Django settings for rafaela_emprende project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.contrib.messages import constants as bootstrapMessages
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'exhlfdat&vfum(-34*c2uroi(($ww(yo$9pv98=e6p^gl(-eoj'
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG_VALUE") == "True"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")

ALLOWED_HOSTS = ["https://rafaela-emprende.herokuapp.com/"]

# For overwriting users default model
AUTH_USER_MODEL = "users.User"

# Application definition

INSTALLED_APPS = [
    # Django Apps
    "django_filters",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_extensions",
    "fontawesomefree",
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
    "haystack",
    # My Apps
    "feed.apps.FeedConfig",
    "users.apps.UsersConfig",
    "entrepreneurs.apps.EntrepreneursConfig",
]

SITE_ID = 1  # Define the site id for django.contrib.sites

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rafaela_emprende.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rafaela_emprende.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if os.environ.get("RUNNING_IN_DOCKER") == "TRUE":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / ".." / ".." / "data" / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": BASE_DIR / "whoosh_index",
    },
}
if os.environ.get("SEARCHBOX_URL"):
    HAYSTACK_CONNECTIONS = {
        "default": {
            "ENGINE": "haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine",
            "URL": os.environ.get("SEARCHBOX_URL"),
            "INDEX_NAME": "documents",
        },
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es-es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# If using in production environment then AWS S3 is used
USE_S3 = os.getenv("USE_S3") == "TRUE"

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_DEFAULT_OVERWRITE = False
    AWS_DEFAULT_ACL = None
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    STATICFILES_DIRS = (BASE_DIR / "static", )
else:
    if os.environ.get("RUNNING_IN_DOCKER") == "TRUE":
        STATIC_URL = "/staticfiles/"
        STATIC_ROOT = BASE_DIR / ".." / ".." / "staticfiles"
        MEDIA_URL = "/media/"
        MEDIA_ROOT = BASE_DIR / ".." / ".." / "media"
        STATICFILES_DIRS = (BASE_DIR / ".." / ".." / "static", )
    else:
        STATIC_URL = "/staticfiles/"
        STATIC_ROOT = BASE_DIR / "staticfiles"
        MEDIA_URL = "/media/"
        MEDIA_ROOT = BASE_DIR / "media"
        STATICFILES_DIRS = (BASE_DIR / "static", )



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
MESSAGE_TAGS = {
    bootstrapMessages.ERROR: "danger",
}


LOGIN_REDIRECT_URL = "feed-home"
LOGIN_URL = "login"


django_heroku.settings(locals())
