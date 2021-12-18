"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from student_management_app import views, adminViews,viewStaff,viewStudent
from student_management_system import settings


urlpatterns = [
    path('homepage', views.showHomePage),
    path('admin/', admin.site.urls),
    path('', views.showLoginPage),
    path('getlogin', views.getlogin),
    path('getUser', views.GetUser),
    path('logout', views.Logout),
    path('adminHome',adminViews.adminHome, name="adminHome"),
    path('addCourse', adminViews.addCourse,name="addCourse"),
    path('saveCourse', adminViews.saveCourse,name="saveCourse"),
    path('manageCourse', adminViews.manageCourse,name="manageCourse"),
    path('editCourse/<str:course_id>', adminViews.editCourse,name="editCourse"),
    path('saveEditedCourse', adminViews.saveEditedCourse,name="saveEditedCourse"),
    path('staffHome', viewStaff.staffHome, name="staffHome"),
    path('studentHome',viewStudent.studentHome, name="studentHome")
]+static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
