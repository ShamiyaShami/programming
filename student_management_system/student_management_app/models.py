from django.db import models

# Create your models here.
class Admin(models.Model):
    admin_id = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class TheStaff(models.Model):
    staff_id = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Courses(models.Model):
    course_id = models.CharField(max_length=50, primary_key=True)
    course_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Student(models.Model):
    student_id = models.CharField(max_length=50, primary_key=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    address = models.TextField(max_length=255)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
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
    subject_id=models.Foreignkey(TaughtCourses,on_delete=models.Do_Nothing)
    attend_date=models.DateTimeField(auto_now_add= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now_add = True)

class AttendanceBookReport(models.Model):
    attendancerprt_id = AutoField(primary_key=True)
    student_id = models.Foreignkey(Student,on_delete=models.DO_NOTHING)
    attendance_id = models.Foreignkey()


class Student_Leave_Report(models.Model)
    Leave_id=models.AutoField(primary_key=True)
    Student_id=models.foreignKey(Student, on_delete=models.CASCADE)
    Date_Of_Leave = models.CharField(max_length=255)
    Reason_For_Leave = models.TextField()
    Status_Of_Leave = models.BooleanField(default=False)
    Created_Date= models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager
