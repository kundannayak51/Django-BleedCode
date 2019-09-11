"""codeManiacs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from Profile import views as users_views
from django.urls import path, include

from django.views.generic import TemplateView
app_name = 'Profile'


urlpatterns = [
    url(r'^(?P<user_id>[a-zA-Z0-9]+)/$',users_views.profile, name='userprofile'),
    #path('saveProfile/', users_views.update_profile, name='saveProfile'),
    url(r'^editprofile/(?P<user_id>[a-zA-Z0-9]+)/$', users_views.update_profile, name='editProfile'),

]