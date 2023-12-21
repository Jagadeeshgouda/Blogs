from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            usern = form.cleaned_data['username']
            userp = form.cleaned_data['password']
            user = authenticate(username= usern, password=userp)

            if user is not None:
                login(request, user)
                return redirect('http://localhost:3000/')

    else:
        form = AuthenticationForm()
    context= {'form':form}
    return render(request, 'login.html', context)



#logout
@login_required(login_url='/')
def logout_form(request):
    logout(request)
    #return redirect('/login')
    return render(request, 'logout.html')

@login_required(login_url='login')
def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('login')
            else:
                return HttpResponse("password is not matching")
        else:
            form = PasswordChangeForm(user= request.user)
            context = {'form':form}
            return render(request, 'changepassword.html',context)
    else:
        return redirect('/changepassword')
    
    
#email authentication

from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import random
from .models import PreRegistration
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def creatingOTP():
    otp = ""
    for i in range(6):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email):
    otp = creatingOTP()
    send_mail(
    'One Time Password',
    f'Hello This is a Blogs project created by jagadeeshgouda Y R with React and Django and Your registration OTP :- {otp}',
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return otp



def createUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                otp = sendEmail(email)
                dt = PreRegistration(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username= form.cleaned_data['username'],email=email,otp=otp,password1 = form.cleaned_data['password1'],password2 = form.cleaned_data['password2'])
                dt.save()
                return HttpResponseRedirect('/verify/')
                
                
        else:
            form = CreateUser()
        return render(request,"newuser.html",{'form':form})
    else:
        return HttpResponseRedirect('/success/')
# def login_function(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = LoginForm(request=request,data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 usr = authenticate(username=username,password = password)
#                 if usr is not None:
#                     login(request,usr)
#                     return HttpResponseRedirect('/success/')
#         else:
#             form = LoginForm()
#         return render(request,'html/login.html',{'form':form})
#     else:
#         return HttpResponseRedirect('/success/')

def verifyUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            if form.is_valid():
                otp = form.cleaned_data['otp']
                data = PreRegistration.objects.filter(otp = otp)
                if data:
                    username = ''
                    first_name = ''
                    last_name = ''
                    email = ''
                    password1 = ''
                    for i in data:
                        print(i.username)
                        username = i.username
                        first_name = i.first_name
                        last_name = i.last_name
                        email = i.email
                        password1 = i.password1

                    user = User.objects.create_user(username, email, password1)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    data.delete()
                    messages.success(request,'Account is created successfully!')
                    return HttpResponseRedirect('/')   
                else:
                    messages.success(request,'Entered OTP is wrong')
                    return HttpResponseRedirect('/verify/')
        else:            
            form = VerifyForm()
        return render(request,'verify.html',{'form':form})
    else:
        return HttpResponseRedirect('/success/')

def success(request):
    if request.user.is_authenticated:
        return render(request,'success.html')
    else:
        return HttpResponseRedirect('/')

from django.db.models import Q

from rest_framework import generics
from .models import BlogPost, BlogContent
from .serializer import BlogPostSerializer, BlogContentSerializer

class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogContentListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer


class BlogContentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogContent.objects.all()
    serializer_class = BlogContentSerializer


# views.py
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm, BlogContentForm

@login_required
def create_blog(request):
    if request.method == 'POST':
        blog_post_form = BlogPostForm(request.POST)
        blog_content_form = BlogContentForm(request.POST, request.FILES)

        if blog_post_form.is_valid() and blog_content_form.is_valid():
            blog_post = blog_post_form.save(commit=False)
            blog_post.user = request.user  # Set the current user
            blog_post.save()

            blog_content = blog_content_form.save(commit=False)
            blog_content.blog_post = blog_post
            blog_content.save()

            return redirect('http://localhost:3000/')  # Redirect to success page or another view

    else:
        blog_post_form = BlogPostForm()
        blog_content_form = BlogContentForm()

    return render(request, 'add.html', {'blog_post_form': blog_post_form, 'blog_content_form': blog_content_form})
