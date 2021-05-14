from .models import admin_model
from .forms import *
from django.conf import settings

from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import re
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    return HttpResponse("Welcome")

def admin_page(request):
    if request.method == "POST":
        form = AdminModel(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    else:
        form = AdminModel()
    return render(request,'admin_page.html',{'form':form})

def advisor_list(request,id):
    content = admin_model.objects.filter(id=id)
    print(content,len(content))
    return render(request,"content.html",{'content':content,'media_url':settings.STATIC_URL})

def call_advisors(request,user_id,advisor_id):
    if request.method == "POST":
        form = BookCall(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("200")
        else:
            return HttpResponse("400")
    else:
        form = BookCall()
    return render(request,'book_call.html',{'form':form})

def booked_calls(request,id):
    cont = admin_model.objects.filter(id=id)
    a = can_book_call.objects.filter(id=id)
    content = {cont:"cont",a:"a"}
    return render(request,"booked_calls.html",{'content':content})

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(email):
    if re.search(regex,email):
        return True
    else:
        return False

reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
def checks_passwd(password1):
    if re.search(reg,password1):
        return True
    else:
        return False


def register(request):
    first_name=""
    last_name=""
    username=""
    password=""
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        username = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists() == False:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password)
            user.save()
            print(first_name,username,password)
            messages.success(request,"Welcome")
            return HttpResponse(status=200)
        else:
            messages.info(request,"User Already Exists")
            return HttpResponse(status=200)
    else:
        return render(request,'try.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['email']
        password1 = request.POST['password1']
        user = authenticate(request,username=username, password=password1)
        print(user)
        if len(password1) == 0 or len(username) == 0:
            messages.info(request,"Field cannot be empty")
            return HttpResponse(status=400)
        elif user is not None:
            login(request,user)
            return HttpResponse(status=200)
        else:
            messages.info(request,"Invalid Credentials")
            return HttpResponse(status=401)
    else:
        return render(request,'registrations/login.html')