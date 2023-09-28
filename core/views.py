from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html', {
        'title': 'Welcome',
    })

def signin(request):
    return render(request, 'core/signin.html', {
        'title': 'Sign in',
    })

def signup(request):
    return render(request, 'core/signup.html', {
        'title': 'Sign up',
    })