from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .import Admin_views 
from .import views
from .import Staff_views
from .import Student_views
urlpatterns = [


     # ADMIN URLs
     #path('admin_demo/',views.admin_demo,name='admindemo'),
     path('accounts/',include('django.contrib.auth.urls')),
     path('doLogin',views.doLogin,name="doLogin"),
     path('login_page',views.ShowLoginPage,name="ShowLogin"),
     path('logout_user/',views.logout_user,name='logout'),
     #path('admin_login/',views.admin_login,name='adminLogin'),
     #path('admin_login_page/',views.admin_login_page,name='adminLoginPage'),
     path('admin_signup_page/',views.signup_admin_page,name='adminSignupPage'),
     path('admin_user_details/',views.admin_user_details,name='adminDetails'),
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
     path('admin_adds_subject_edit_save',Admin_views.add_subject_edit, name='AdminAddSubjectEditSave'),
 

     path('admin_add_session_manage/', Admin_views.add_session_manage, name='AdminAddSessionManage'),
     path('admin_add_session_save/', Admin_views.add_session_save, name='AdminAddSessionSave'),

     path('check_user_availabilty/', views.check_user_availability, name='CheckUserAvailabilty'),
     path('check_email_availabilty/', views.check_email_availability, name='CheckEmailAvailabilty'),
     
     path('student_feedback_message/', Admin_views.student_feedback_message, name='StudentFeedbackMessage'),
     path('student_feedback_message_replied/', Admin_views.student_feedback_message_replied, name='StudentFeedbackMessageReplied'),
     path('faculty_feedback_message/', Admin_views.faculty_feedback_message, name='FacultyFeedbackMessage'),
     path('faculty_feedback_message_replied/', Admin_views.faculty_feedback_message_replied, name='FacultyFeedbackMessageReplied'),
     path('student_leave_view/', Admin_views.student_leave_view, name='StudentLeaveView'),
     path('faculty_leave_view/', Admin_views.faculty_leave_view, name='FacultyLeaveView'),
     path('student_leave_approve/<str:leave_id>/', Admin_views.student_leave_approve, name='StudentLeaveApprove'),
     path('faculty_leave_approve/<str:leave_id>/', Admin_views.faculty_leave_approve, name='FacultyLeaveApprove'),
     path('student_leave_disapprove/<str:leave_id>/', Admin_views.student_leave_disapprove, name='StudentLeaveDisapprove'),
     path('faculty_leave_disapprove/<str:leave_id>/', Admin_views.faculty_leave_disapprove, name='FacultyLeaveDisapprove'),

     path('admin_view_attendance', Admin_views.admin_view_attendance, name="AdminViewAttendance"),
     path('admin_get_attendance_dates', Admin_views.admin_get_attendance_dates,name="AdminGetAttendanceDates"),
     path('admin_get_attendance_student', Admin_views.admin_get_attendance_student,name="AdminGetAttendanceStudents"),
     
     path('admin_profile', Admin_views.admin_profile,name="AdminProfile"),
     path('admin_profile_save', Admin_views.admin_profile_save,name="AdminProfileSave"),

     
     # STAFF URLs
     path('faculty_signup_page/',views.signup_faculty_page,name='facultySignupPage'),
     path('staff_home/',Staff_views.staff_home,name='staffHome'),
     path('staff_take_attendance/',Staff_views.staff_take_attendance,name='StaffTakeAttendance'),
     path('faculty_save_attendance_data/', Staff_views.save_attendance, name="FacultySaveAttendance"),
     #path('faculty_update_attendance_data/', Staff_views.update_attendance, name="FacultySaveAttendance"),
     path('faculty_fetch_student/', Staff_views.fetch_student, name="FacultyFetchStudent"),
     path('faculty_get_attendance_dates/', Staff_views.get_attendance, name="FacultyGetAttendance"),
     path('faculty_update_attendance_data/', Staff_views.update_attendance, name="FacultyUpdateAttendance"),
     path('faculty_updated_attendance/', Staff_views.updated_attendance, name="FacultyUpdatedAttendance"),    
     path('get_students/', Staff_views.get_students, name="FacultyGetStudents"),
     path('faculty_apply_leave/', Staff_views.apply_leave, name="FacultyApplyLeave"),
     path('faculty_apply_leave_save/', Staff_views.apply_leave_save, name="FacultyApplyLeaveSave"),
     path('faculty_feedback/', Staff_views.feedback, name="FacultyFeedback"),
     path('faculty_feedback_save/', Staff_views.feedback_save, name="FacultyFeedbackSave"),
     path('faculty_edit_profile/',Staff_views.edit_profile,name='StaffEditProfile'),
     path('faculty_edit_profile_save/',Staff_views.edit_profile_save,name='StaffEditProfileSave'),
     path('faculty_todo_list/',Staff_views.todo_list,name='FacultyTodoList'),
     path('faculty_share_notes/', Staff_views.share_notes, name="FacultyShareNotes"),
     path('faculty_share_notes_save/', Staff_views.share_notes_save, name="FacultyShareNotesSave"),
     
      
     # STUDENT URLs
     path('student_home/',Student_views.student_home,name='studentHome'),
     path('student_signup_page/',views.signup_student_page, name='studentSignupPage'),
     path('student_view_attendance', Student_views.student_view_attendance, name="StudentViewAttendance"),
     path('student_view_attendance_post', Student_views.student_view_attendance_post, name="StudentViewAttendancePost"),
     path('student_apply_leave/', Student_views.apply_leave, name="StudentApplyLeave"),
     path('student_apply_leave_save/', Student_views.apply_leave_save, name="StudentApplyLeaveSave"),
     path('student_feedback/', Student_views.feedback, name="StudentFeedback"),
     path('student_feedback_save/', Student_views.feedback_save, name="StudentFeedbackSave"),   
     path('student_edit_profile/',Student_views.edit_profile,name='StudentEditProfile'),
     path('student_edit_profile_save/',Student_views.edit_profile_save,name='StudentEditProfileSave'),
     path('student_todo_list/',Student_views.todo_list,name='StudentTodoList'),
     path('student_download_notes/',Student_views.download_notes,name='StudentDownloadNotes'),
]
    