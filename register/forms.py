from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'name': 'floating_email','id':'floating_email','class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'})),
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
                                   'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
                                            'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '
                                            'dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 '
                                            'dark:text-white'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border '
                                                                                          'border-gray-300 '
                                                                                          'text-gray-900 text-sm '
                                                                                          'rounded-lg '
                                                                                          'focus:ring-blue-500 '
                                                                                          'focus:border-blue-500 '
                                                                                          'block w-full p-2.5 '
                                                                                          'dark:bg-gray-600 '
                                                                                          'dark:border-gray-500 '
                                                                                          'dark:placeholder-gray-400 '
                                                                                          'dark:text-white'}))

