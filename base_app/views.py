from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from dal import autocomplete

from .models import Entity, User
from .forms import CustomLoginForm, RegisterForm, CustomUserCreationForm


def home(request):
    return render(request, 'home.html')


def logout_button(request):
    logout(request)
    return render(request, 'home.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contactus(request):
    return render(request, 'contactus.html')


def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        # print(form)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            print(user)

            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', None)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('landing_app:landing')
            else:
                messages.error(
                    request, 'The username or password is incorrect')
        else:
            messages.error(request, "Form invalid. Check form errors")
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                logout(request)

            user = form.save()
            login(request, user)

            return render(request, 'registration_success.html')
    else:
        if request.user.is_authenticated:
            logout(request)
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.entity = request.user.userprofile.entity
            user = form.save()
            data = {
                'success': True,
                'message': "User created successfully",
            }
            return JsonResponse(data)
        else:
            errors_html = {field: '\n'.join(errors)
                           for field, errors in form.errors.items()}
            data = {'success': False, 'errors_html': errors_html,
                    'message': "Error creating user"}
            return JsonResponse(data, status=400)
    else:
        form = CustomUserCreationForm()
        return render(request, 'register_user.html', {'form': form})
