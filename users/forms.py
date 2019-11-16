from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import UserprofileInfo


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class Userprofile(forms.ModelForm):

    class Meta():
        model = UserprofileInfo
        fields = ('protfoils_site', 'ready', 'pic')


