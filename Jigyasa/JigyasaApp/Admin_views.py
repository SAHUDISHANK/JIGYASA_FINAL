import json
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import AddStudentForm, EditStudentForm
from . models import Attendance, AttendanceReport, CustomUser,Courses, FeedBackStaffs, FeedBackStudent, LeaveReportStaff, LeaveReportStudent, SessionYearModel, Students,Subjects,Staffs
from django.core.files.storage import FileSystemStorage



def home(request):
    student_count = Students.objects.all().count()
    print(student_count)
    subject_count = Subjects.objects.all().count()
    staff_count = Staffs.objects.all().count()
    course_count = Courses.objects.all().count()
    course_all = Courses.objects.all()
    course_name_list = []
    subject_count_list = []
    student_count_list_in_course = []
    for course in course_all:
        subjects = Subjects.objects.filter(course_id=course.id).count()
        students = Students.objects.filter(course_id=course.id).count()
        course_name_list.append(course.course_name)
        subject_count_list.append(subjects)
        student_count_list_in_course.append(students)
    print('Subjects Count List')
    print(subject_count_list)
    print('Student Count List in course')
    print(student_count_list_in_course)
    print('course name list')
    print(course_name_list)
    subjects_all = Subjects.objects.all()
    subject_list = []
    student_count_list_in_subject = []
    for subject in subjects_all:
        course = Courses.objects.get(id=subject.course_id.id)
        student_count_subject = Students.objects.filter(course_id=course.id).count()
        subject_list.append(subject.subject_name)
        student_count_list_in_subject.append(student_count_subject)
    print('subject List')
    print(subject_list)
    print('student count in subjects')
    print(student_count_list_in_subject)
    # Staff Parameters
    staffs = Staffs.objects.all()
    attendance_present_list_staff = []
    attendance_absent_list_staff = []
    staff_name_list = []
    for staff in staffs:
        subject_ids = Subjects.objects.filter(staff_id=staff.admin.id)
        attendance = Attendance.objects.filter(subject_id__in=subject_ids).count()
        leaves = LeaveReportStaff.objects.filter(staff_id=staff.id, leave_status=1).count()
        attendance_present_list_staff.append(attendance)
        attendance_absent_list_staff.append(leaves)
        staff_name_list.append(staff.admin.username)

    students_all = Students.objects.all()
    attendance_present_list_student = []
    attendance_absent_list_student = []
    student_name_list = []
    for student in students_all:
        attendance = AttendanceReport.objects.filter(student_id=student.id, status=True).count()
        absent = AttendanceReport.objects.filter(student_id=student.id, status=False).count()
        leaves = LeaveReportStudent.objects.filter(student_id=student.id, leave_status=1).count()
        attendance_present_list_student.append(attendance)
        attendance_absent_list_student.append(leaves+absent)
        student_name_list.append(student.admin.username)
    param = {
        "student_count": student_count,
        "staff_count": staff_count,
        "subject_count": subject_count,
        "course_count": course_count,
        "course_name_list": course_name_list,
        "subject_count_list": subject_count_list,
        "student_count_list_in_course": student_count_list_in_course,
        "student_count_list_in_subject": student_count_list_in_subject,
        "subject_list": subject_list,
        "staff_name_list": staff_name_list,
        "attendance_present_list_staff": attendance_present_list_staff,
        "attendance_absent_list_staff": attendance_absent_list_staff,
        "student_name_list": student_name_list,
        "attendance_present_list_student": attendance_present_list_student,
        "attendance_absent_list_student": attendance_absent_list_student
        }

    return render(request, 'dashboard/admin/home_content.html', param)

def add_faculty(request):
    return render(request,'dashboard/admin/add_staff.html')

def add_course(request):
    return render(request,'dashboard/admin/add_course.html')
    
def add_student(request):
    # courses=Courses.objects.all()
    form = AddStudentForm()
    return render(request,'dashboard/admin/add_student.html',{"form":form})

def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,'dashboard/admin/add_subject.html',{'courses':courses,'staffs':staffs})
 
def edit_faculty(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"dashboard/admin/edit_faculty.html",{"staff":staff,"id":staff_id})    

def edit_student(request,student_id): 
    request.session['student_id']=student_id
    student=Students.objects.get(admin=student_id)  
    form = EditStudentForm() 
    form.fields['email'].initial = student.admin.email
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['address'].initial = student.address
    form.fields['courses'].initial = student.course_id.id
    form.fields['sex'].initial = student.gender
    form.fields['session_year_id'].initial=student.session_year_id.id
    return render(request,"dashboard/admin/edit_student.html",{"form":form,"id":student_id,"username":student.admin.username} )    
 

def edit_course(request,course_id):   
    course=Courses.objects.get(id = course_id)
    return render(request,"dashboard/admin/edit_course.html",{"course":course,"id":course_id} )    
 

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

def add_session_manage(request):
    return render(request, 'dashboard/admin/manage_session.html')


 


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
        form = AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email_address = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            address = form.cleaned_data.get('address')
            password = form.cleaned_data.get('password')
            course_id = form.cleaned_data.get('courses')
            session_id = form.cleaned_data.get('session_year_id')
            sex = form.cleaned_data.get('sex')
            
            print(sex)
            
            try: 
                user = CustomUser.objects.create_user(user_type=3, username=username, first_name=first_name,
                                                        last_name=last_name, email=email_address, password=password)
                course_obj = Courses.objects.get(id=course_id)
                user.students.course_id = course_obj
                user.students.gender = sex
                session=SessionYearModel.objects.get(id=session_id)
                user.students.session_year = session
                user.students.address = address
                user.save()
                messages.success(request, "Successfully Added Student") 
                return HttpResponseRedirect('/app/admin_add_student_add')
            except Exception as e:
                messages.error(request, e)
                messages.error(request, "Failed To Add Student.Please Try Again!!")
                return HttpResponseRedirect('/app/admin_add_student_add')
        
        else:
            form= AddStudentForm(request.POST)
            return render(request,'dashboard/admin/add_student.html',{"form":form})

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

def add_session_save(request):
    if request.method != "POST":
        return HttpResponseRedirect("/app/admin_add_session_manage")
    else:
        session_start_year= request.POST.get("session_start")
        session_end_year= request.POST.get("session_end")
        try:
            sessionyear = SessionYearModel(session_start_year = session_start_year , session_end_year = session_end_year)
            sessionyear.save()
            messages.success(request,"successfully added session")
            return HttpResponseRedirect(reverse("AdminAddSessionManage"))
        except:
             messages.error(request,"Failed to  added session")
             return HttpResponseRedirect(reverse("AdminAddSessionManage"))

 

   
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
        student_id=request.session.get("student_id")
        if student_id is None:
            print('Studentid None')
            return HttpResponseRedirect("/app/admin_add_student_manage/")


        form = EditStudentForm(request.POST,request.FILES) 
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email_address = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            address = form.cleaned_data.get('address')
            course_id = form.cleaned_data.get('courses')
            session_id = form.cleaned_data.get('session_year_id')
            sex = form.cleaned_data.get('sex')
            
            try:  
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email=email_address
                user.save()

                student = Students.objects.get(admin =student_id )
                student.address = address
                session=SessionYearModel.objects.get(id=session_id)
                user.students.session_year = session
                student.gender=sex
                courses = Courses.objects.get(id=course_id)
                student.course_id = courses
                student.save()
                del request.session['student_id']
                messages.success(request, "Successfully Edited Student")
                return HttpResponseRedirect("/app/admin_add_student_edit/"+student_id) 
            except Exception as e:
                messages.error(request, e)
                messages.error(request, "Failed To Edit Student.Please Try Again!!")
                return HttpResponseRedirect("/app/admin_add_student_edit/"+student_id) 
        
        else :
            form = EditStudentForm(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request,"dashboard/admin/edit_student.html",{"form":form,"id":student_id,"username":student.admin.username} )    


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


def faculty_feedback_message(request):
    feedbacks=FeedBackStaffs.objects.all()
    return render(request,"dashboard/admin/faculty_feedback.html",{"feedbacks":feedbacks})

def student_feedback_message(request):
    feedbacks=FeedBackStudent.objects.all()
    return render(request,"dashboard/admin/student_feedback.html",{"feedbacks":feedbacks})


@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")

@csrf_exempt
def faculty_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStaffs.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
    

def faculty_leave_view(request):
    leaves=LeaveReportStaff.objects.all()
    return render(request,"dashboard/admin/faculty_leave_view.html",{"leaves":leaves})

def student_leave_view(request):
    leaves=LeaveReportStudent.objects.all()
    return render(request,"dashboard/admin/student_leave_view.html",{"leaves":leaves})

def student_leave_approve(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("StudentLeaveView"))

def student_leave_disapprove(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("StudentLeaveView"))


def faculty_leave_approve(request,leave_id):
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("FacultyLeaveView"))

def faculty_leave_disapprove(request,leave_id):
    leave=LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("FacultyLeaveView"))


def admin_view_attendance(request):
    subjects=Subjects.objects.all()
    session_year_id=SessionYearModel.objects.all()
    return render(request,"dashboard/admin/admin_view_attendance.html",{"subjects":subjects,"session_year_id":session_year_id})


@csrf_exempt
def admin_get_attendance_dates(request):
    subject=request.POST.get("subject")
    session_year_id=request.POST.get("session_year_id")
    subject_obj=Subjects.objects.get(id=subject)
    session_year_obj=SessionYearModel.objects.get(id=session_year_id)
    attendance=Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)


@csrf_exempt
def admin_get_attendance_student(request):
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
    


def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"dashboard/admin/admin_profile.html",{"user":user})
 
def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("AdminProfile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            # if password!=None and password!="":
            #     customuser.set_password(password)
            customuser.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("AdminProfile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("AdminProfile"))