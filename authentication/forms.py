from django import forms
class LoginForm(forms.Form):
    """Log in existing user"""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)