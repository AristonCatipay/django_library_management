from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'core/index.html', {
        'title': 'Welcome',
    })

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # User is authenticated.
            auth.login(request, user)
            return redirect('core:index')
        else: 
            # Invalid credentials
            messages.info(request, 'Invalid credentials.')
            return redirect('core:signin')
            
    return render(request, 'core/signin.html', {
        'title': 'Sign in',
    })

def signup(request):
    return render(request, 'core/signup.html', {
        'title': 'Sign up',
    })