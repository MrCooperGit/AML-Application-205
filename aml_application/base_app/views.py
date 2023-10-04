from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from .models import
from .forms import LoginForm, RegisterForm


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print("Login successful")
            messages.success(request, 'Login successful')
            return redirect('/index')

        else:
            print("Login failed")
            messages.error(request, 'Login failed')
            return redirect('/login')

    else:
        print("not post")
        form = LoginForm(request)

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful')

            return redirect('/login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})
