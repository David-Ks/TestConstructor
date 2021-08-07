from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(max_length=100, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	password2 = forms.CharField(max_length=100, label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
	username = forms.CharField(max_length=100, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))