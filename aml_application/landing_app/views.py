from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .utils import get_available_apps
from base_app.models import AvailableApps
from .models import UserTab
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request, app_name=None):

    available_apps = get_available_apps()
    open_tabs = UserTab.objects.filter(user=request.user)
    user = request.user

    if app_name is None:
        # means user is at /landing
        # need to redirect to /landing/[first app in database]/ if database is not empty else /landing/default_app
        # this will restart the process and the app name will be set, skipping this if statement
        if len(open_tabs) > 0:
            app_name = open_tabs[0].app_id.name
            return redirect(f'/landing/{app_name}/')
        else:
            app_name = 'default_app'
    else:
        # means user is at /landing/[app name]
        # need to render the app template if the app name is valid else redirect to /landing to restart the process
        if not any(tab.app_id.name == app_name for tab in open_tabs):
            return redirect('/landing')

    # user is here if app name is valid
    # format the app_template in preparation for rendering
    app_template_name = f'{app_name}.html'

    available_apps_obj = AvailableApps.objects.all()
    open_user_tabs_obj = UserTab.objects.filter(user=request.user).select_related('app_id')
    
    # setting the active tab in the database
    for tab in open_user_tabs_obj:
        if tab.app_id.name == app_name:
            tab.is_active = True
        else:
            tab.is_active = False
        tab.save()
    
    return render(request, 'landing.html', {
        'app_template_name': app_template_name,
        'available_apps': available_apps_obj,
        'tabs': open_user_tabs_obj,
        'user': request.user,
    })


@login_required
def add_tab(request, app_name_to_add=None):
    if app_name_to_add is None:
        return redirect('/landing')

    available_apps = get_available_apps()
    if app_name_to_add not in available_apps:
        return redirect('/landing')

    tab_exists = UserTab.objects.filter(
        user=request.user, app_id=AvailableApps.objects.get(name=app_name_to_add)).exists()
    if tab_exists:
        # future: ask if you want to start form again
        return redirect(f'/landing/{app_name_to_add}/')

    # add tab to UserTab
    tab = UserTab(user=request.user, app_id=AvailableApps.objects.get(
        name=app_name_to_add), is_active=True)
    tab.save()

    return redirect(f'/landing/{app_name_to_add}/')


@login_required
def delete_tab(request, tab_to_delete=None):
    if tab_to_delete is None:
        return redirect('/landing')

    tab = get_object_or_404(UserTab, user=request.user,
                            app_id=AvailableApps.objects.get(name=tab_to_delete))
    tab.delete()

    return redirect('/landing')
