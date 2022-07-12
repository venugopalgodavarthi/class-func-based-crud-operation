from email import message
from django.conf import settings
from django.shortcuts import render, redirect
from authe.forms import registerform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.


def registerview(request):
    form = registerform()
    if request.method == 'POST' and request.FILES:
        form = registerform(request.POST, request.FILES)
        if form.is_valid():
            subject = "welcome to myshow"
            name = request.POST['username']
            messages = f'Hi Mr/Ms{name}, thank you for registartion my show site'
            send_mail(subject=subject, message=messages, from_email=settings.EMAIL_HOST,
                      recipient_list=['venugopalgodavarthi@gmail.com', ])
            # form.save()

            return redirect('/login/')
    return render(request, 'register.html', {'form': form})


def loginview(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/home/')
    return render(request, 'register.html', {'form': form})


@login_required(login_url='/login/')
def homeview(request):
    return render(request, 'home.html')


@login_required(login_url='/login/')
def logoutview(request):
    logout(request)
    return redirect('/login/')
