from django.shortcuts import render


def staffHome(request):
    return render(request,"Staff_Register/home.html")