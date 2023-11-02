from functools import wraps
from django.http import HttpResponse


def require_entity(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user_profile = request.user.userprofile
        if user_profile.entity:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("You do not have access to this page.")

    return _wrapped_view
