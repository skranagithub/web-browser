from click import password_option
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from blog_app import urls,views
from django.contrib import messages
from django.shortcuts import render
from blog_app.models import Post
from django.views import generic
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
# Create your views here.


def home(request):  
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        number = request.POST['number']
        password = request.POST['password']
        Confirmpassword = request.POST['Confirmpassword']
        if password == Confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.set_password(password)
                user.is_staff=True
                user.save()
                print(username,password)
                return redirect('login_user')
    else:            
        return render(request,'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        Password = request.POST['Password']
        
        user = auth.authenticate(username=username,password=Password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('post_detail')
        else:
            messages.info(request,'Invalid Email or Password')
            return redirect('login_user')
    else:
            
        return render(request,'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index1.html'
    
class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'    
