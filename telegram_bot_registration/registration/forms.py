from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(max_length=255, label='Login')
    password = forms.CharField(max_length=255, label='Password', widget=forms.PasswordInput)
