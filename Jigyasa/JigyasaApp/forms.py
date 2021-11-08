from django import forms
from .models import Courses, SessionYearModel

class DateInput(forms.DateInput):
    input_type = 'date'

class AddStudentForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'})) 
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_list = []
    try:
        courses=Courses.objects.all()

        for course in courses:
            small_course = (course.id, course.course_name)
            course_list.append(small_course)
    except:    
            course_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )
    session_list = []
    try:
        sessions=SessionYearModel.objects.all()
        for session in sessions:
            session_start_year = str(session.session_start_year)
            session_start_year = session_start_year[:4]
            session_end_year = str(session.session_end_year)
            session_end_year = session_end_year[:4]
            small_session = (session.id, session_start_year + "-" + session_end_year)
            session_list.append(small_session)
    except:
        session_list=[]
    print(session_list)
    courses= forms.ChoiceField(label="Course",choices = course_list)
    sex= forms.ChoiceField(label="sex",choices = gender_choice)
    session_year_id = forms.ChoiceField(label='Select Session', choices=session_list,widget=forms.Select(attrs={'class': 'form-control'}))
   

class EditStudentForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_list = []
    try: 
        courses=Courses.objects.all()

        for course in courses:
            small_course = (course.id, course.course_name)
            course_list.append(small_course)
    except:    
            course_list = []
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    )
    session_list = []
    try:
        sessions=SessionYearModel.objects.all()
        for session in sessions:
            session_start_year = str(session.session_start_year)
            session_start_year = session_start_year[:4]
            session_end_year = str(session.session_end_year)
            session_end_year = session_end_year[:4]
            small_session = (session.id, session_start_year + "-" + session_end_year)
            session_list.append(small_session)
    except:
        session_list=[]
    print(session_list)
    courses= forms.ChoiceField(label="Course",choices = course_list)
    sex= forms.ChoiceField(label="sex",choices = gender_choice)
    session_year_id = forms.ChoiceField(label='Select Session', choices=session_list,widget=forms.Select(attrs={'class': 'form-control'}))