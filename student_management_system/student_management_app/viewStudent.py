from django.shortcuts import render


def studentHome(request):
    return render(request,"student register/student_home_content.html")