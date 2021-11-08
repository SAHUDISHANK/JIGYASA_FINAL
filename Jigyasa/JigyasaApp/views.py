from django import http
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout
from .models import CustomUser
from .custom_backend import EmailBackEnd
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
# For Faculty sign-up page

def signup_faculty_page(request):
    return render(request, 'JigyasaApp/faculty_signup_page.html')

# admin signup page

def signup_admin_page(request):
    return render(request, 'JigyasaApp/admin_signup_page.html')

# For Student sign-up page

def signup_student_page(request):
    return render(request, 'JigyasaApp/student_signup_page.html')

# Login Pages
# Function for student login page

# def student_login_page(request):
#     return render(request, 'JigyasaApp/student_login_page.html')

# Function for faculty login page



# admin login page


# student login

# def student_login(request):
#     pass

# faculty login

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/app/admin_home_page')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staffHome"))
            else:
                return HttpResponseRedirect(reverse("studentHome"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect('/app/login_page')


def admin_user_details(request):
    if request.user != None:
        return HttpResponse("User:" + request.user.email + "Usertype:" + request.user.user_type)
 

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def ShowLoginPage(request):
    return render(request, 'JigyasaApp/faculty_login_page.html')
# def faculty_user_details(request):
#     if request.user != None:
#         return HttpResponse("User:" + request.user.email + "Usertype:" + request.user.user_type)


# admin login


# def admin_login(request):
#     if request.method != 'POST':
#         return HttpResponse('Method not allowed')
#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('pass')
#         print(email)
#         print(password)
#         get_user = EmailBackEnd.authenticate(request, username=email, password=password)
#         print(get_user)

#         if get_user != None:
#             login(request,get_user)
#             return HttpResponseRedirect('/app/admin_home_page')
#         else:
#             messages.error(request,"Invalid login Credentials")
#             return HttpResponseRedirect('/app/admin_login_page')

# User details Admin


def admin_demo(request):
    return render(request,'dashboard/demo.html')
    

def check_user_availability(request):
    if request.method == "POST":
        username = request.POST.get('username')
        print('username:'+str(username))
        all_users=CustomUser.objects.all()
        username_list=[]
        for user in all_users:
            username_list.append(user.username)
        
        if username in username_list:
            status={'status':'no'}
            response=json.dumps(status)
        else:
            status={'status':'yes'}
            response=json.dumps(status)
        return HttpResponse(response)
    else:
        return HttpResponse('Method Not allowed')
      
def check_email_availability(request):
    if request.method == "POST":
        email = request.POST.get('email')
        print('email:'+str(email))
        all_users=CustomUser.objects.filter(email=email).exists() 
        print(all_users)
        if all_users:
            print('Exist')
            status={'status':'no'}
            response=json.dumps(status)
        else:
            print('Not Exist')
            status={'status':'yes'}
            response=json.dumps(status)
        return HttpResponse(response)
    else:
        return HttpResponse('Method Not allowed')