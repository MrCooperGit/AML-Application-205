from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import require_entity
from dal import autocomplete

from .models import UserProfile, User, Customer
from .forms import LoginForm, RegisterForm, CustomUserCreationForm


def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # print(form)

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            messages.error(
                request, 'The username or password is incorrect', extra_tags='no_clear_messages')

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print("user not none")
                login(request, user)
                return redirect('base_app:index')
            else:
                messages.error(
                    request, 'The username or password is incorrect', extra_tags='no_clear_messages')
                # request.do_not_clear_messages = True
                print("not authenticated")
                return redirect('base_app:login')
        else:
            if form.errors:
                print(form.errors)
                print("There are errors")
                errors = form.errors
                print(errors)
            print("Form not valid")
    else:
        form = LoginForm(request=request)

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(
                    request, 'A user with this email address already exists.')
                return redirect('base_app:register')

            user = form.save()

            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('base_app:index')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form, 'messages': messages.get_messages(request)})


@login_required
@require_entity
def register_user(request):
    if request.method == 'POST':
        # Pre-fill the 'entity' field with the logged-in user's entity
        form = CustomUserCreationForm(
            request.POST, initial={'entity': request.user.userprofile.entity})
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base_app:index')
    else:
        # Pre-fill the 'entity' field with the logged-in user's entity
        form = CustomUserCreationForm(
            initial={
                'entity': request.user.userprofile.entity,
                'first_name': '',
                'last_name': '',
            }
        )

    return render(request, 'register_user.html', {'form': form})
