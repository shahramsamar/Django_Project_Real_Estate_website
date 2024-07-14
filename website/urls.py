"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from website.views import *
from django.conf.urls import handler400, handler403, handler404, handler500

app_name = 'website'



urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('property', property_view, name='property'),
    path('newsletter',newsletter_view, name='newsletter'),

]


# Custom error handler
handler400 = 'website.views.custom_400'
handler403 = 'website.views.custom_403'
handler404 = 'website.views.custom_404'
handler500 = 'website.views.custom_500'