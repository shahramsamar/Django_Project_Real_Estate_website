from core.settings import *







INSTALLED_APPS = [
    'multi_captcha_admin',
    'compressor',
    'captcha',
]


# captcha admin setting
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'statics'
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