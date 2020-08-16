from django.db import models
from django.forms import ModelForm
from django.conf import settings


# Create your models here.

class ask(models.Model):
    username = models.CharField(max_length=50)
    ques = models.TextField(max_length=500)
    image = models.ImageField(upload_to='ques/',max_length=50)
    files = models.FileField(upload_to='files/',max_length=50)

class profile(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    workplace = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='image/',max_length=50)
    text = models.TextField(max_length=500)
    achievements = models.FileField(upload_to='files/',max_length=50)