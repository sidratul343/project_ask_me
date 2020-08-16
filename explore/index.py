from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from database.forms import pro,proo
from database.models import profile,ask
from django.conf import settings
from django.contrib import messages
from django.db import connection
from django.core.mail import send_mail,EmailMessage
from .settings import *
from django.contrib.auth import logout
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def front(request):
    return render(request,'front.html')

def log_in(request):
    if request.method == 'POST':

        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Please type your USERNAME and PASSWORD properly!")
            return redirect('login')
    else:
        return render(request,'login.html')

def reg(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['repsw']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username has already been taken")
                return redirect('reg')
            else:
                user = User.objects.create_user(username=username,email=email,password=pass1)
                user.save();
                messages.info(request,'registration done successfully')
                return redirect('login')
        else:
            messages.info(request,'password does not match!')
            return redirect('reg')
    else:
        return render(request,'reg.html')
    
def home(request):
    return render(request,'home.html')

def profile_(request):
    if request.method == 'POST':
        username=request.POST['uname']
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        gender=request.POST['gender']
        occupation=request.POST['occupation']
        address=request.POST['clas']
        department=request.POST['dept']
        workplace=request.POST['workplace']
        picture=request.FILES['img']
        text=request.POST['description']
        achievements=request.FILES['files']
        if request.user.username == username:

            profilee = profile(username=username,name=name,age=age,email=email,gender=gender,occupation=occupation,address=address,department=department,workplace=workplace,picture=picture,text=text,achievements=achievements)
            profilee.save()
           
            return redirect('home')
        else:
            messages.info(request,'wrong username!')
            return redirect('profile')
    else:
        return render(request,'profile.html')

def main_page(request):
    dests = profile.objects.all().order_by("-id")
    
    return render(request,"main_page.html",{'dests':dests})


def asked(request):
    if request.method == 'POST':
        username=request.user.username
        email=request.user.email
        ques=request.POST['description']
        try:
            image=request.FILES['img']
            prof = ask(username=username,ques=ques,image=image,email=email)
        except:
            prof = ask(username=username,ques=ques,email=email)
        
        prof.save();
        return redirect('explore_ques')
        
    else:
        return render(request,'ask.html')



def explore(request):
    ddests = ask.objects.all().order_by("-id")
    return render(request,"explore_ques.html",{'ddests':ddests})


def logoutuser(request):
    auth.logout(request)
    return redirect('/')

def personal(request):
    dest = profile.objects.all().filter(username=request.user.username)
    return render(request,"personal.html",{'dest':dest})

def update(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.age=request.POST['age']
        t.email=request.POST['email']
        t.gender=request.POST['gender']
        t.occupation=request.POST['occupation']
        t.address=request.POST['clas']
        t.department=request.POST['dept']
        t.workplace=request.POST['workplace']
        t.picture=request.FILES['img']
        t.text=request.POST['description']
        t.achievements=request.FILES['files']
        t.save(update_fields=['age','email','email','gender','occupation','address','department','workplace','picture','text','achievements'])
        return redirect('personal')

    else:
        return render(request,'update.html')

def update_age(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.age=request.POST['age']
        t.save(update_fields=['age'])
        return redirect('personal')
    else:    
        return render(request,'update_age.html')

def update_department(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.department=request.POST['dept']
        t.save(update_fields=['department'])
        return redirect('personal')
    else:    
        return render(request,'update_department.html')


def update_gender(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.gender=request.POST['gender']
        t.save(update_fields=['gender'])
        return redirect('personal')
    else:    
        return render(request,'update_gender.html')


def update_address(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.address=request.POST['clas']
        t.save(update_fields=['address'])
        return redirect('personal')
    else:    
        return render(request,'update_address.html')


def update_email(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.email=request.POST['email']
        t.save(update_fields=['email'])
        return redirect('personal')
    else:    
        return render(request,'update_email.html')

def update_bio(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.text=request.POST['description']
        t.save(update_fields=['text'])
        return redirect('personal')
    else:    
        return render(request,'update_bio.html')

def update_dp(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.picture=request.FILES['img']
        t.save(update_fields=['picture'])
        return redirect('personal')
    else:    
        return render(request,'update_dp.html')


def update_workplace(request):
    if request.method == 'POST':
        t = profile.objects.get(username=request.user)
        t.workplace=request.POST['workplace']
        t.save(update_fields=['workplace'])
        return redirect('personal')
    else:    
        return render(request,'update_workplace.html')

