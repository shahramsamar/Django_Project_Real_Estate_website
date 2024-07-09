from core.settings import *
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG") 

ALLOWED_HOSTS = ['*']


DATABASES = {
        'default': {
            'ENGINE': config("DB_ENGINE"),
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD':config("DB_PASSWORD"),
            'HOST': config("DB_HOST"),
            'PORT': config("DB_PORT", cast=int),
        }
    }


# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': config("DB_ENGINE"),
#             'NAME': config("DB_NAME"),
#             'USER': config("DB_USER"),
#             'PASSWORD':config("DB_PASSWORD"),
#             'HOST': config("DB_HOST"),
#             'PORT': config("DB_PORT", cast=int),
#         }
#     }






# captcha admin setting
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]



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

# sitemap framework # this is needed active site framework
# robots # this is needed active site framework
ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = True # false -> how to show sitemap






# AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend',
                           'accounts.backends.EmailBackend']


EMAIL_BACKEND = config("EMAIL_BACKEND")
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS")
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")


# security deploy
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True