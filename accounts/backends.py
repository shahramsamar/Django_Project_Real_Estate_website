from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q
from django.http import HttpRequest

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs: Any):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=username)|Q(username=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None    
            