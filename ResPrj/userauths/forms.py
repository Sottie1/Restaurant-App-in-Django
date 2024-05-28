from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# class SignUpForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
#     email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
#     password1 = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Pasword"}))
#     password2 = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Confirm Password"}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')


User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')