from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from student_management_app.models import Courses

def adminHome(request):
    return render(request,"Admin/home.html")

def addCourse(request):
    return render(request,"Admin/addCourses.html")

def saveCourse(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model=Courses(course_name=course)
            course_model.save()
            messages.success(request,"Course Successfully Added")
            return HttpResponseRedirect(reverse("addCourse"))
        except:
            messages.error(request,"Failed To Add Course, please try again")
            return HttpResponseRedirect(reverse("addCourse"))

def manageCourse(request):
    courses=Courses.objects.all()
    return render(request,"Admin/manageCourse.html",{"courses":courses})


def editCourse(request,course_id):
    course=Courses.objects.get(course_id=course_id)
    return render(request,"Admin/editCourse.html",{"course":course,"id":course_id})

def saveEditedCourse(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(course_id=course_id)
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect(reverse("editCourse",kwargs={"course_id":course_id}))
        except:
            messages.error(request,"Failed to Edit Course")
            return HttpResponseRedirect(reverse("editCourse",kwargs={"course_id":course_id}))