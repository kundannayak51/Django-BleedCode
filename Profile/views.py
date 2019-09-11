from django.shortcuts import render
from django.contrib.auth.models import User
from Profile.models import Profile
from django.views.generic import DetailView, ListView, View
from django.contrib.auth.decorators import login_required
from  django.db import transaction
from .forms import UserForm,ProfileForm
from django.contrib import messages
from django.shortcuts import render, redirect


from django.views.generic.edit import FormView
# Create your views here.


def profile(request,user_id):
    #user = User.objects.get(username = user_id)

    user = User.objects.get(id=user_id)
    p = Profile.objects.get(user=user)
    p1 = p.profilePicture
    return render(request, 'profile.html', {'user': user,'p1':p1})


@login_required
@transaction.atomic
def update_profile(request,user_id):
    if request.method == 'POST':
        user_form = UserForm(request.POST,request.FILES,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('Profile:userprofile', user_id=user_id)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'editprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


'''def editProfile(request,user_id):
    user = User.objects.get(id = user_id)
    print(user_id)
    print(user.email)
    if request.method == 'POST':
       print("AAA")

    else:

        print("bbbb")
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'editprofile.html',{'user': user,'user_form': user_form,
        'profile_form': profile_form})
'''