from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save

# Create your models here.
class MainUser(AbstractUser):
    userData = ((1,"Admin"),(2,"Staff"),(3,"Student"))
    userType  = models.CharField(default=1,choices=userData,max_length=50)

class Admin(models.Model):
    adm_id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(MainUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class TheStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(MainUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(MainUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    address = models.TextField(max_length=255)
    picture = models.FileField()
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class TaughtCourses(models.Model):
    subject_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(TheStaff, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add=True) 
    objects = models.Manager()

class StudentNotification(models.Model):
    stud_not_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StaffNotification(models.Model):
    staf_not_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(TheStaff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttendanceBook(models.Model):
    attendance_id= models.AutoField(primary_key= True)
    subject_id=models.ForeignKey(TaughtCourses,on_delete=models.DO_NOTHING)
    attend_date=models.DateTimeField(auto_now_add= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now_add = True)
    objects = models.Manager()


class AttendanceBookReport(models.Model):
    attendancerprt_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(AttendanceBook,on_delete=models.CASCADE)
    attendance_status = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()


class Student_Leave_Report(models.Model):
    Leave_id=models.AutoField(primary_key=True)
    Student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    Date_Of_Leave = models.CharField(max_length=255)
    Reason_For_Leave = models.TextField()
    Status_Of_Leave = models.BooleanField(default=False)
    Created_Date= models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StaffFeedback(models.Model):
    staff_feedback_id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(TheStaff, on_delete=models.CASCADE)
    staff_feedback = models.TextField()
    Feedback_reply = models.TextField()
    Created_date= models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StudentFeedback(models.Model):
    stud_feedback_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    stud_feedback = models.TextField()
    Feedback_reply = models.TextField()
    Created_date= models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Staff_Leave_Report(models.Model):
    Leave_id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(TheStaff, on_delete=models.CASCADE)
    Date_Of_Leave = models.CharField(max_length=255)
    Reason_For_Leave = models.TextField()
    Status_Of_Leave = models.BooleanField(default=False)
    Created_Date= models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

@receiver(post_save,sender=MainUser)
def createUserProfile(sender,instance,created,**kwargs):
    if created:
        if instance.userType==1:
            Admin.objects.create(admin=instance)
        if instance.userType==2:
            TheStaff.objects.create(admin=instance)
        if instance.userType==3:
            Student.objects.create(admin=instance)

@receiver(post_save,sender=MainUser)
def saveUserProfile(sender,instance,**kwargs):
    if instance.userType==1:
        instance.admin.save()
    if instance.userType==2:
        instance.thestaff.save()
    if instance.userType==3:
        instance.student.save()

            

