from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "JigyasaApp.Admin_views":
                    pass
                elif modulename == "JigyasaApp.views":
                    pass
                else:
                    return HttpResponseRedirect("/app/admin_home_page/")
            elif user.user_type == "2":
                if modulename == "JigyasaApp.Staff_views":
                    pass
                elif modulename == "JigyasaApp.views":
                    pass
                else:
                    return HttpResponseRedirect("/app/staff_home/")
            elif user.user_type == "3":
                if modulename == "JigyasaApp.Student_views":
                    pass
                elif modulename == "JigyasaApp.views":
                    pass
                else:
                    return HttpResponseRedirect("/app/student_home/")
            else:
                return HttpResponseRedirect(reverse("show_login"))

        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login"):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))