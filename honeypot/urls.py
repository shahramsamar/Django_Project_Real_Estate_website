from django.urls import path, include,re_path
from honeypot import views

app_name = "honey"

urlpatterns = [
    path("login/",views.LoginView.as_view(),name="login" ),
    re_path("^",views.RedirectToLogin.as_view()),
]
