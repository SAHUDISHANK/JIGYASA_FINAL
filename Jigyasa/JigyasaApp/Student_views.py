from django.shortcuts import render


def student_home(request):
    return render(request,"dashboard/student_template/student_home_template.html"  )