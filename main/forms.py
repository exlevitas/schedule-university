from django import forms
from .models import *


class GetEmail(forms.ModelForm):
    author = forms.CharField(max_length=50, label='How shall we name you?', required=True)
    email = forms.CharField(max_length=50, label='Enter your email', required=True)

    class Meta:
        model = Email
        fields = ['author', 'email']