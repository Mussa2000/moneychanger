from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from helpers.submit_helper import SubmitButtonHelper


class UserCreationForm(SubmitButtonHelper,forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), help_text='User will receive a password change link after creation', initial='JustAnotherPassword2023!@#')

    class Meta:
        model = get_user_model()
        fields = ['email','username','first_name', 'last_name',  'password','is_staff', ]
