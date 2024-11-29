from django import forms
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'address', 'customer', 'assigned_persons']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Přidání pole pro email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']