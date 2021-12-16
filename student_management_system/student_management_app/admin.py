from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import MainUser

# Register your models here.
class UserModel(UserAdmin):
    pass
admin.site.register(MainUser,UserModel)