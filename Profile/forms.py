from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profilePicture', 'institution', 'country')