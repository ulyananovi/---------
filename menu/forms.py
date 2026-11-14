from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, label="ФИО")
    email = forms.EmailField(label="Почта")
    
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email')

class CustomAuthenticationForm(AuthenticationForm):
    pass