from django import forms
from django.forms import ModelForm
from database.models import profile,ask
from django.contrib.auth import authenticate
from django.forms import Textarea,RadioSelect,ChoiceField

class pro(ModelForm):
    class Meta:
        model = profile
        fields = "__all__"
        
        
class proo(ModelForm):
    class Meta:
        model = ask
        fields = "__all__"
        