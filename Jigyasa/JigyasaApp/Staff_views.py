from django.shortcuts import render


def staff_home(request):
    return render(request,"dashboard/staff_template/staff_home_template.html")