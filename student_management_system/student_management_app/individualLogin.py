from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class individualLogin(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        moduleName=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.userType == "1":
                if moduleName == "student_management_app.adminViews":
                    pass
                elif moduleName == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("adminHome"))
            elif user.userType == "2":
                if moduleName == "student_management_app.StaffViews":
                    pass
                elif moduleName == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staffHome"))
            elif user.userType == "3":
                if moduleName == "student_management_app.studentviews":
                    pass
                elif moduleName == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("studentHome"))
            else:
                return HttpResponseRedirect(reverse("showLoginPage"))

        else:
            if request.path == reverse("showLoginPage") or request.path == reverse("getlogin"):
                pass
            else:
                return HttpResponseRedirect(reverse("showLoginPage"))