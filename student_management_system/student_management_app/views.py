from django import http
from django.contrib.auth import login, authenticate, logout
#from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from student_management_app.loginAuth import LoginAuth

#from student_management_app.loginAuth import LoginAuth

# Create your views here.

def showHomePage(request):
    return render(request,  "homepage.html")

def showLoginPage(request):
    return render(request, "login.html")

def getlogin(request):
    if request.method != "POST":
        return HttpResponse("Wrong Method! Method not POST")
    else:
        user = LoginAuth.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            if user.userType == "1":
                return HttpResponseRedirect('/adminHome')
            elif user.userType == "2":
                return HttpResponseRedirect('/staffHome')
            elif user.userType == "3":
                return HttpResponseRedirect('/studentHome')
            #login(request, user)
            #return HttpResponse("Email: " + request.POST.get("email") + "Password: " + request.POST.get("password"))
        else:

            return HttpResponse("Wrong Credentials")

def GetUser(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + "userType: " + str(request.user.userType))
    else:
        return HttpResponse("Enter Login Details")

def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")