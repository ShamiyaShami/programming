from django.shortcuts import render

# Create your views here.

def showHomePage(request):
    return render(request,"homepage.html")
