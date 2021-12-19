from django.shortcuts import render


def student_home(request):
    return render(request,"student register/student_home_content.html")