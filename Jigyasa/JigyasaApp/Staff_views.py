from django.shortcuts import render

from . models import Subjects




def staff_home(request):
    return render(request,"dashboard/staff_template/staff_home_template.html")

def staff_take_attendance(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    return render(request,"dashboard/staff_template/staff_take_attendance.html")

