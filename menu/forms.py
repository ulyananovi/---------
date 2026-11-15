from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100, 
        label="ФИО", 
        widget=forms.TextInput(attrs={'class': 'form-style', 'placeholder': 'Иванов Иван Иванович'}),
        error_messages={'required': 'Пожалуйста, введите ФИО.'}
    )
    email = forms.EmailField(
        label="Почта", 
        widget=forms.EmailInput(attrs={'class': 'form-style', 'placeholder': 'example@mail.ru'}),
        error_messages={'required': 'Пожалуйста, введите почту.', 'invalid': 'Введите корректный адрес почты.'}
    )
    
    class Meta:
        model = User
        fields = ('username', 'full_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-style', 'placeholder': 'Ваш логин'}),
        }
        error_messages = {
            'username': {
                'required': 'Пожалуйста, введите логин.',
                'unique': 'Пользователь с таким логином уже существует.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Минимум 8 символов'})
        self.fields['password2'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Повторите пароль'})
        self.fields['password1'].label = "Пароль"
        self.fields['password2'].label = "Повтор пароля"
        
        self.fields['password1'].error_messages = {'required': 'Пожалуйста, введите пароль.'}
        self.fields['password2'].error_messages = {
            'required': 'Пожалуйста, повторите пароль.',
            'password_mismatch': 'Пароли не совпадают.',
        }

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Введите логин'})
        self.fields['password'].widget.attrs.update({'class': 'form-style', 'placeholder': 'Введите пароль'})
        self.fields['username'].label = "Логин"
        self.fields['password'].label = "Пароль"
        
        self.error_messages['invalid_login'] = "Неверный логин или пароль."
        self.error_messages['inactive'] = "Этот аккаунт отключен."