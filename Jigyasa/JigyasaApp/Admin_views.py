from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from . models import CustomUser,Courses, Students,Subjects,Staffs
from django.core.files.storage import FileSystemStorage
from . forms import AddStudentForm

def home(request):
    return render(request,'dashboard/admin/home_content.html')

def add_faculty(request):
    return render(request,'dashboard/admin/add_staff.html')

def add_course(request):
    return render(request,'dashboard/admin/add_course.html')
    
def add_student(request):
    courses=Courses.objects.all()
    return render(request,'dashboard/admin/add_student.html',{'courses':courses})

def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,'dashboard/admin/add_subject.html',{'courses':courses,'staffs':staffs})

def edit_faculty(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"dashboard/admin/edit_faculty.html",{"staff":staff,"id":staff_id})    

def edit_student(request,student_id):
    courses=Courses.objects.all()
    student=Students.objects.get(admin=student_id)
    return render(request,"dashboard/admin/edit_student.html",{"student":student,"courses":courses} )    
 

def edit_course(request,course_id):   
    course=Courses.objects.get(id = course_id)
    return render(request,"dashboard/admin/edit_course.html",{"course":course} )    
 

def edit_subject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"dashboard/admin/edit_subject.html",{"subject":subject,"staffs":staffs,"courses":courses,"id":subject_id})    
 




def add_faculty_manage(request):
    staffs=Staffs.objects.all()
    return render(request, 'dashboard/admin/manage_faculty.html',{'staffs':staffs})

def add_student_manage(request):
    students=Students.objects.all()
    return render(request, 'dashboard/admin/manage_student.html',{'students':students})

def add_course_manage(request):
    courses=Courses.objects.all()
    return render(request, 'dashboard/admin/manage_course.html',{'courses':courses})

def add_subject_manage(request):
    subjects=Subjects.objects.all()
    return render(request, 'dashboard/admin/manage_subject.html',{'subjects':subjects})





def add_faculty_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/app/admin_add_faculty_page")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/app/admin_add_faculty_page")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model=Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect("/app/admin_add_course_save")
        except:
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect("/app/admin_add_course_save")

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, 'Method not Allowed')
        return HttpResponse("/app/admin_add_student_add")
    else:
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email_address = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        password = request.POST.get('password')
        course_id = request.POST.get('course')
        session_start = request.POST.get('session_start_date')
        session_end = request.POST.get('session_end_date')
        sex = request.POST.get('sex')
        cnf_password = request.POST.get('password1')
      

        if password == cnf_password:
            try:
                user = CustomUser.objects.create_user(user_type=3, username=username, first_name=first_name,
                                                      last_name=last_name, email=email_address, password=cnf_password)
                course_obj = Courses.objects.get(id=course_id)
                user.students.course_id = course_obj
                user.students.gender = sex 
                user.students.session_start_year = session_start
                user.students.session_end_year = session_end
                user.students.address = address
                user.students.profile_pic = ""
                user.save()
                messages.success(request, "Successfully Added Student")
                return HttpResponseRedirect('/app/admin_add_student_add')
            except:
                messages.error(request, "Failed To Add Student.Please Try Again!!")
                return HttpResponseRedirect('/app/admin_add_student_add')
        else:
            messages.error(request, "Passwords Not Matched!!")
            return HttpResponseRedirect('/app/admin_add_student_add')

def add_subject_save(request):
    if request.method != "POST":
        messages.error(request, 'Method not Allowed')
        return HttpResponse("/app/admin_add_subject_add")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get("staff")
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject = Subjects(subject_name=subject_name, course_id=course, staff_id=staff)
            subject.save()
            messages.success(request, "Successfully Added Subject")
            return HttpResponseRedirect("/app/admin_add_subject_add")
        except:
            messages.error(request, "Failed to Add Subject")
            return HttpResponseRedirect("/app/admin_add_subject_add")




def add_faculty_edit(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect("/app/admin_add_faculty_edit/"+staff_id) 
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect("/app/admin_add_faculty_edit/"+staff_id)

def add_student_edit(request):    
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email_address = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        course_id = request.POST.get('change_course')
        session_start = request.POST.get('session_start_date')
        session_end = request.POST.get('session_end_date')
        sex = request.POST.get('sex')
        
        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email=email_address

            student = Students.objects.get(admin =student_id )
            student.address = address
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.gender=sex
            course = Courses.objects.get(id = course_id)
            student.course_id = course
            student.save()
            messages.success(request, "Successfully Edited Student")
            return HttpResponseRedirect("/app/admin_add_student_edit/"+student_id) 
        except:
            messages.error(request, "Failed To Edit Student.Please Try Again!!")
            return HttpResponseRedirect("/app/admin_add_student_edit/"+student_id) 

def add_course_edit(request):   
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect("/app/admin_add_course_edit/"+course_id) 
        except:
            messages.error(request,"Failed to Edit Course")
            return HttpResponseRedirect("/app/admin_add_course_edit/"+course_id) 

def add_subject_edit(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        subject_name=request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request,"Successfully Edited Subject")
            return HttpResponseRedirect("/app/admin_add_subject_edit/"+subject_id)
        except:
            messages.error(request,"Failed to Edit Subject")
            return HttpResponseRedirect("/app/admin_add_subject_edit/"+subject_id)