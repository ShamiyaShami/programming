from django.shortcuts import render


def student_home(request):
    return render(request,"structure_template/student_home_content.html")