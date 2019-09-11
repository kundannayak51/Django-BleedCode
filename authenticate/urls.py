from django.urls import path, include
from django.conf.urls import url
from .views import *
from . import views

#app_name = 'BleedCode'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    path('signUp/', views.signUp, name='signUp'),
    path('finalsignup/', views.signUp, name='finalsignup'),
    #url(r'^editProfile/', views.editProfile, name ='editProfile'),
    #url(r'^editProfile/(?P<user_id>[a-zA-Z0-9]+)/$', views.editProfile, name ='editProfile'),

    path('accounts/login', views.my_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')), # This will include many urls like login,logout
]