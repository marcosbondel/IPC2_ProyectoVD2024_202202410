from django import forms


class LoginForm(forms.Form):
    uid = forms.CharField(label='uid')
    password = forms.CharField(widget=forms.PasswordInput(), label='password')