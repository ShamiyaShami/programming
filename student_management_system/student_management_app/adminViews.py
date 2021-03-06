from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from student_management_app.forms import AddStudent_Form, EditStudent_Form
from django.core.files.storage import FileSystemStorage
from student_management_app.models import Courses, MainUser, TheStaff, Student, TaughtCourses

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
            user= MainUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,userType=2)
            user.TheStaff.address=address
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
            return HttpResponseRedirect(reverse("StaffEdit",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("StaffEdit",kwargs={"staff_id":staff_id}))


def AddStudent(request):
    form=AddStudent_Form()
    return render(request,"Admin/AddStudent.html",{"form":form})

def AddStudent_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudent_Form(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            course_id=form.cleaned_data["course"]
            sex=form.cleaned_data["sex"]

            picture=request.FILES['picture']
            fs=FileSystemStorage()
            filename=fs.save(picture.name,picture)
            profile_pic_url=fs.url(filename)

            try:
                user=MainUser.objects.createUser(username=username,password=password,email=email,last_name=last_name,first_name=first_name,userType=3)
                user.Student.address=address
                course_obj=Courses.objects.get(course_id=course_id)
                user.Student.course_id_id=course_obj
                user.Student.gender=sex
                user.Student.picture=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Student")
                return HttpResponseRedirect(reverse("AddStudent"))
            except:
                messages.error(request,"Failed to Add Student")
                return HttpResponseRedirect(reverse("AddStudent"))
        else:
            form=AddStudent_Form(request.POST)
            return render(request, "Admin/AddStudent.html", {"form": form})


def ManageStudent(request):
    students = Student.objects.all()
    return render(request,"Admin/ManageStudent.html",{"students":students})


def editStudent(request,student_id):
    request.session['student_id']=student_id
    student=Student.objects.get(admin=student_id)
    form=EditStudent_Form()
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id_id.id
    form.fields['sex'].initial=student.gender
    return render(request,"Admin/EditStudent.html",{"form":form,"id":student_id,"username":student.admin.username})

def saveEditedStudent(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id=request.session.get("student_id")
        if student_id==None:
            return HttpResponseRedirect(reverse("ManageStudent"))

        form=EditStudent_Form(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            course_id = form.cleaned_data["course"]
            sex = form.cleaned_data["sex"]

            if request.FILES.get('picture',False):
                picture=request.FILES['picture']
                fs=FileSystemStorage()
                filename=fs.save(picture.name,picture)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            try:
                user=MainUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.username=username
                user.email=email
                user.save()

                student=Student.objects.get(admin=student_id)
                student.address=address
                student.gender=sex
                course=Courses.objects.get(course_id=course_id)
                student.course_id=course
                if profile_pic_url!=None:
                    student.picture=profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request,"Successfully Edited Student")
                return HttpResponseRedirect(reverse("editStudent",kwargs={"student_id":student_id}))
            except:
                messages.error(request,"Failed to Edit Student")
                return HttpResponseRedirect(reverse("editStudent",kwargs={"student_id":student_id}))
        else:
            form=EditStudent_Form(request.POST)
            student=Student.objects.get(admin=student_id)
            return render(request,"Admin/EditStudent.html",{"form":form,"student_id":student_id,"username":student.admin.username})


def addSubject(request):
    courses=Courses.objects.all()
    staff=MainUser.objects.filter(userType=2)
    return render(request,"Admin/addSubject.html",{"TheStaff":staff,"Courses":courses})

def saveSubject(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(course_id=course_id)
        staff_id=request.POST.get("staff")
        staff=MainUser.objects.get(id=staff_id)

        try:
            subject=TaughtCourses(subject_name=subject_name,course_id_id=course,staff_id_id=staff)
            subject.save()
            messages.success(request,"Successfully Added Subject")
            return HttpResponseRedirect(reverse("addSubject"))
        except:
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect(reverse("addSubject"))


def manageSubject(request):
    subjects=TaughtCourses.objects.all()
    return render(request,"Admin/ManageSubject.html",{"subjects":subjects})


def editSubject(request,subject_id):
    subject=TaughtCourses.objects.get(subject_id=subject_id)
    courses=Courses.objects.all()
    staffs=MainUser.objects.filter(userType=2)
    return render(request,"Admin/EditSubject.html",{"subject":subject,"staffs":staffs,"courses":courses,"id":subject_id})

def saveEditedSubject(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject=TaughtCourses.objects.get(id=subject_id)
            subject.subject_name=subject_name
            staff=MainUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request,"Successfully Edited Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"editSubject":subject_id}))
        except:
            messages.error(request,"Failed to Edit Subject")
            return HttpResponseRedirect(reverse("editSubject",kwargs={"subject_id":subject_id}))

