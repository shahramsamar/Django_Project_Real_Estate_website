from core.settings import *
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DEBUG") 
DEBUG = True


ALLOWED_HOSTS = ['*']


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
#             'ENGINE': config("DB_ENGINE",default='django.db.backends.postgresql'),
#             'NAME': config("DB_NAME",default='project'),
#             'USER': config("DB_USER",default='postgres'),
#             'PASSWORD':config("DB_PASSWORD",default='0000'),
#             'HOST': config("DB_HOST",default='127.0.0.1'),
#             'PORT': config("DB_PORT",cast=int,default='5432'),
#         }
#     }


DATABASES = {
        'default': {
            'ENGINE': config("DB_ENGINE",default='django.db.backends.postgresql'),
            'NAME': config("DB_NAME",default='asus'),
            'USER': config("DB_USER",default='postgres'),
            'PASSWORD':config("DB_PASSWORD",default='123'),
            'HOST': config("DB_HOST",default='127.0.0.1'),
            'PORT': config("DB_PORT",cast=int,default='5432'),
        }
    }




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

# sitemap framework  and robots # this is needed active site framework
ROBOTS_USE_HOST = True # false -> how to show
ROBOTS_USE_SITEMAP = True # false -> how to show sitemap
SITE_ID = 2 # or whatever the ID of your Site object is

 




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
CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True #to avoid transmitting the session cookie over HTTP accidentally.

# Cross site scripting (XSS)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True


