from urllib import request
from django.forms import ModelForm
from .models import CourtFile, File
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django .contrib.auth.models import User
from django import forms

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

class FileForm(ModelForm):
    signature = forms.TextInput()
    type = forms.TextInput()
    scan = forms.FileField()
    class Meta:
        model = File
        fields = ['signature', 'type', 'scan']


#class AccessForm(ModelForm):
#    class Meta:
#        model = AccessRequest
#        fields = ['user', 'signature', 'description']

class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={
        'id': 'file_id'
    }))



