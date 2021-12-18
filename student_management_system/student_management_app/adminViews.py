from django.shortcuts import render

def adminHome(request):
    return render(request,"Admin/home.html")