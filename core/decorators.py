from django.http import HttpResponse
from django.shortcuts import redirect

# A decorator is a function that takes another function as a parameter.

def unauthenticated_user(view_function):
    # If you are authenticated you will not be able to view the page.
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:index')
        else:   
            return view_function(request, *args, **kwargs)
    return wrapper_function