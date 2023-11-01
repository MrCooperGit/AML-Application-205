from django.shortcuts import render, redirect

# Create your views here.

def index(request, app_name=None):
    # TODO: Add check to database to make sure the app name is valid to prevent malicious requests
    app_database = [
        # tmp, replacement for db check
        'cddForm',
    ]
    
    if app_name is None:
        # means user is at /landing
        # need to redirect to /landing/[first app in database]/ if database is not empty else /landing/default_app
        # this will restart the process and the app name will be set, skipping this if statement
        if len(app_database) > 0:
            app_name = app_database[0]
            return redirect(f'/landing/{app_name}/')
        else:
            app_name = 'default_app'
    else:
        # means user is at /landing/[app name]
        # need to render the app template if the app name is valid else redirect to /landing
        if app_name not in app_database:
            return redirect('/landing')

    # format the app_template in preparation for rendering
    app_template_name = f'{app_name}.html'
    
    return render(request, 'landing.html', {'app_template_name': app_template_name})