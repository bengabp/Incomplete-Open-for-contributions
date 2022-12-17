from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import DevhubAccount


class DevhubAccountCreationForm(UserCreationForm):
    class Meta:
        model = DevhubAccount
        fields = (
            "username", "email", 'first_name', 'last_name', 'password', 'profile_picture_web_path', 'github_profile_url',
            'linkedin_profile_url')


class DevhubAccountChangeForm(UserChangeForm):
    class Meta:
        model = DevhubAccount
        fields = (
            "username", "email", 'first_name', 'last_name', 'password', 'profile_picture_web_path', 'github_profile_url',
            'linkedin_profile_url')
