from django import forms
from users.models import Client
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ['username', 'email', 'password1', 'password2']