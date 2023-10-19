from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .utils import get_available_apps
from base_app.models import AvailableApps
from .models import UserTab
from django.contrib.auth.models import User

# Create your views here.

def index(request, app_name=None):
    
    available_apps = get_available_apps()
    
    if app_name is None:
        # means user is at /landing
        # need to redirect to /landing/[first app in database]/ if database is not empty else /landing/default_app
        # this will restart the process and the app name will be set, skipping this if statement
        if len(available_apps) > 0:
            app_name = str(available_apps[0])
            return redirect(f'/landing/{app_name}/')
        else:
            app_name = 'default_app'
    else:
        # means user is at /landing/[app name]
        # need to render the app template if the app name is valid else redirect to /landing to restart the process
        if app_name not in available_apps:
            return redirect('/landing')
    
    # user is here if app name is valid
    # format the app_template in preparation for rendering
    app_template_name = f'{app_name}.html'

    return render(request, 'landing.html', {'app_template_name': app_template_name})

def add_tab(request, app_name_to_add=None):
    if app_name_to_add is None:
        return redirect('/landing')
    
    available_apps = get_available_apps()
    if app_name_to_add not in available_apps:
        return redirect('/landing')
    
    tab_exists = UserTab.objects.filter(user=request.user).exists()
    if tab_exists:
        # future: ask if you want to start form again
        redirect(f'/landing/{app_name_to_add}/')
    
    # add tab to UserTab
    tab = UserTab(user=request.user, app_id=AvailableApps.objects.get(name=app_name_to_add), is_active=True)
    tab.save()
    
    return redirect(f'/landing/{app_name_to_add}/')
    