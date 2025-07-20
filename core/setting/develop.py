from core.settings import *
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bz07lkpxolqg(g+a05x)chk($v=#vmtm9y=n*cm4*q=a45pzez'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']





INSTALLED_APPS = [
    'django.contrib.contenttypes',  # Must be present
    'django.contrib.auth',          # Should come before contenttypes
    # ... other apps ...
    'taggit',                      # Required for taggit
    'website',     
    # added module for dev 
    'django_extensions',
    # location after staticfiles
    'debug_toolbar',# Your app
]




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'




# compressor
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
# Set the backend to use for compression
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]
# Cache settings for compressor
COMPRESS_CACHE_BACKEND = 'default'


# debug_toolbar setting for dev when trun on it activate and trun off deactivate
# INTERNAL_IPS = [
#     # ...
#     "127.0.0.1",
#     # ...
# ]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }