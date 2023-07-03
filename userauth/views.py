from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is already used")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email is already in used")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('allbooks')
        else:
            messages.info(request, 'passwords are not same')
            return redirect('register')
    else:
        return render(request, 'user/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('allbooks')
        else:
            messages.info(request, 'some thing went wrong')
            return redirect('login')
    else:
        return render(request, 'user/login.html')


def logout(request):
    auth.logout(request)
    return redirect('allbooks')