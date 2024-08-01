from django.conf import settings


HONEY_LOGIN_TRYOUT = getattr(settings, "HONEY_LOGIN_TRYOUT", 5)
