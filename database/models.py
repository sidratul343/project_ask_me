from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class profile(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    workplace = models.CharField(max_length=50,null=True,blank=True)
    picture = models.ImageField(upload_to='image/',max_length=50,null=True,blank=True)
    text = models.TextField(max_length=500,null=True,blank=True)
    achievements = models.FileField(upload_to='files/',max_length=50,null=True,blank=True)
    

class ask(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    ques = models.TextField(max_length=500,blank=True, null=True)
    image = models.ImageField(upload_to='ques/',max_length=50,null = True,blank = True)
    files = models.FileField(upload_to='files/',max_length=50,null = True,blank = True)

