from django.shortcuts import render

def Homepage_For_Staff(request):
    return render(request, "Staff_Register/home.html")