from django.contrib import admin
from django.urls import path
from django.conf import settings
from .import Admin_views 
from .import views
urlpatterns = [
     path('admin_demo/',views.admin_demo,name='admindemo'),

     path('admin_login/',views.admin_login,name='adminLogin'),
     path('admin_login_page/',views.admin_login_page,name='adminLoginPage'),
     path('admin_signup_page/',views.signup_admin_page,name='adminSignupPage'),

     path('admin_user_details/',views.admin_user_details,name='adminDetails'),
     path('admin_user_logout/',views.admin_user_logout,name='adminLogout'),

     path('admin_home_page/',Admin_views.home,name='adminHome'),

     path('admin_add_faculty_page/',Admin_views.add_faculty, name='AdminAddFaculty'),
     path('admin_add_faculty_save/',Admin_views.add_faculty_save, name='AdminAddFacultySave'),
     path('admin_add_faculty_manage/',Admin_views.add_faculty_manage, name='AdminAddFacultyManage'),
     path('admin_add_faculty_edit/<str:staff_id>',Admin_views.edit_faculty, name='AdminAddFacultyEdit'),
     path('admin_add_faculty_edit_save',Admin_views.add_faculty_edit, name='AdminAddFacultyEditSave'),

     path('admin_add_course_add/',Admin_views.add_course, name='AdminAddCourse'),
     path('admin_add_course_save/',Admin_views.add_course_save, name='AdminAddCourseSave'),
     path('admin_add_course_manage/', Admin_views.add_course_manage, name='AdminAddCourseManage'),
     path('admin_add_course_edit/<str:course_id>',Admin_views.edit_course, name='AdminAddCourseEdit'),
     path('admin_add_course_edit_save',Admin_views.add_course_edit, name='AdminAddCourseEditSave'),

     path('admin_add_student_add/',Admin_views.add_student, name='AdminAddStudent'),
     path('admin_add_student_save/',Admin_views.add_student_save, name='AdminAddStudentSave'),
     path('admin_add_student_manage/', Admin_views.add_student_manage, name='AdminAddStudentManage'),
     path('admin_add_student_edit/<str:student_id>',Admin_views.edit_student, name='AdminAddStudentEdit'),
     path('admin_add_student_edit_save',Admin_views.add_student_edit, name='AdminAddStudentEditSave'),

     path('admin_add_subject_add/',Admin_views.add_subject, name='AdminAddSubject'),
     path('admin_add_subject_save/',Admin_views.add_subject_save, name='AdminAddSubjectSave'),
     path('admin_add_subject_manage/',Admin_views.add_subject_manage, name='AdminAddSubjectManage'),
     path('admin_add_subject_edit/<str:subject_id>',Admin_views.edit_subject, name='AdminAddSubjectEdit'),
     path('admin_add_subject_edit_save',Admin_views.add_subject_edit, name='AdminAddSubjectEditSave'),
 


     path('student_login/',views.student_login,name='studentLogin'),
     path('student_login_page/',views.student_login_page, name='studentLoginPage'),
     path('student_signup_page/',views.signup_student_page, name='studentSignupPage'),
     
     path('faculty_login_page/',views.faculty_login_page, name='facultyLoginPage'),
     path('faculty_login/',views.faculty_login, name='facultyLogin'),
     path('faculty_signup_page/',views.signup_faculty_page, name='facultySignupPage'),
        
]