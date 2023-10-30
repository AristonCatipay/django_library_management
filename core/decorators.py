from django.http import HttpResponse
from django.shortcuts import redirect

# A decorator is a function that takes another function as a parameter.

# If you are authenticated you will not be able to view the page.
def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')
        else:   
            return view_function(request, *args, **kwargs)
    return wrapper_function

# It will only allow groups that are stated to view the page.
def allow_certain_groups(allowed_groups=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page.')
        return wrapper_function
    return decorator