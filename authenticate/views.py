from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from Profile import forms
from Profile import models
from Profile import *
from Profile.models import Profile
from Profile.forms import UserForm,ProfileForm

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('home')

    else:
        # Return an 'invalid login' error message.
        return redirect('login')


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})



def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
            #return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request,'registration/signup.html', {'form': form})
    #return HttpResponseRedirect('/')


