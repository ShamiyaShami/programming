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
    id = models.AutoField(primary_key=True)
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
