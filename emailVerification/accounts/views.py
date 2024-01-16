from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import timedelta
# Create your views here.
@login_required
def home(request):
    print(str(uuid.uuid4()))
    return render(request, 'home.html')

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login/')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login/')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login/')
        
        auth_login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        Password = request.POST.get('password')
        print(username, email, Password)

        try:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken.')
                return redirect(request, '/register/')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect(request, '/register/')

            user_obj = User(username=username, email=email)
            user_obj.set_password(Password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            
            profile_obj = Profile.objects.create(user=user_obj, auth_token = auth_token)
            profile_obj.save()

            send_mail_after_registration(email, auth_token)

            return redirect('/token/')
        except Exception as e:
            print(e)


    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def token_send(request):
    return render(request, 'token_send.html')

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login/')

            if profile_obj.is_verification_link_valid():
                profile_obj.is_verified = True
                profile_obj.save()
                messages.success(request, 'Your account has been verified.')
                return redirect('/login/')
            else:
                messages.error(request, 'Verification link has expired. Please request a new one.')
                return redirect('/error/')
        else:
            return redirect('/error/')
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred during verification.')
        return redirect('/error/')

def error_page(request):
    return render(request, 'error.html')

def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
