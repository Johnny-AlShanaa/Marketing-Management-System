# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models

from .models import Marketer

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Marketer
        fields = ("user_name", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Marketer
        fields = ("user_name", "email")
