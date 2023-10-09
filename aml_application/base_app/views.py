from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserProfile, User
from .forms import LoginForm, RegisterForm


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('/index')
            else:
                messages.error(request, 'Login failed')
                return redirect('/login')
    else:
        form = LoginForm(request)

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, 'A user with this email address already exists.')
                return redirect('/register')

            user = form.save()
            user_profile = UserProfile.objects.create(
                user=user, user_type=form.cleaned_data['userType'])
            # Manually create a user session after registration
            request.session['user_id'] = user.id

            messages.success(request, 'Registration successful')
            return redirect('/index')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'messages': messages.get_messages(request)})
