from socket import fromshare
from django.forms import ModelForm
from .models import CourtFile
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django .contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CourtfileForm(ModelForm):
    court = forms.TextInput()
    signature = forms.TextInput()
    article = forms.TextInput()
    contents_list = forms.FileField()
    class Meta:
        model = CourtFile
        fields = ['court', 'signature', 'article', 'contents_list']
        labels = {
            'court': 'Wybierz sąd',
            'signature': 'Sygnatura',
            'article': 'Artykuł',
            'contents_list': 'Plik z zawartością'
        }
