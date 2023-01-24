from importlib.resources import contents
from turtle import title
from unittest.util import _MAX_LENGTH
import xdrlib
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Court(models.Model):
    court_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    governor = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.court_name

class CourtFile(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE, null=True)
    signature = models.CharField(max_length=200, null=True)
    article = models.CharField(max_length=200, null=True)
    contents_list = models.FileField(upload_to = "C:\\Users\\Gabrysia\\Desktop\\Dev\\denv\\inz\\users\\cfiles\\contents", null=True)

    def __str__(self):
        return f'{self.court} - {self.signature}'

class File(models.Model):
    signature = models.ForeignKey(CourtFile, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=200, null=True)
    scan = models.FileField(upload_to = "C:\\Users\\Gabrysia\\Desktop\\Dev\\denv\\inz\\users\\cfiles\\files", null=True)

    def __str__(self):
        return f'{self.signature} ({self.type})'

class Expert(models.Model):
    speciality = models.CharField(max_length=200, null=True)
    specialisation = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    ex_title = models.CharField(max_length=200, null=True)
    term = models.DateField(null=True)
    locality = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.surname} {self.name}'

class ExpertsStatement(models.Model):
    signature = models.ForeignKey(CourtFile, on_delete=models.CASCADE, null=True)
    scan = models.FileField(upload_to = "C:\\Users\\Gabrysia\\Desktop\\Dev\\denv\\inz\\users\\cfiles\\statements", null=True, blank=True)
    statement_title = models.CharField(max_length=200, null=True)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.statement_title

class AccessRequest(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, default="oczekująca")
    signature = models.ForeignKey(CourtFile, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.signature} {self.user}'
