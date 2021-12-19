from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from student_management_app.models import Courses, MainUser, TheStaff

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

def addStaff(request):
    return render(request,"Admin/AddStaff.html")


def save_Staff(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user= MainUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect(reverse("addStaff"))
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect(reverse("addStaff"))


def staff_Manage(request):
    staff = TheStaff.objects.all()
    return render(request,"Admin/staffManager.html",{"staffs":staff})


def staffEdit(request,staff_id):
    staff=TheStaff.objects.get(admin=staff_id)
    return render(request, "Admin/Staff_Edit.html", {"staff":staff,"id":staff_id})


def saveEditedStaff(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        address = request.POST.get("address")

        try:
            user = MainUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model = TheStaff.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect(reverse("staffEdit",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("staffEdit",kwargs={"staff_id":staff_id}))

