from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from .models import
# from .forms import SignupForm, LoginForm


def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')
