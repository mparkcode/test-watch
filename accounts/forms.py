from django import forms


class UserLoginForm(forms.Form):
    """Form is for user login"""
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)