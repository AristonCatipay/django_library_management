from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html', {
        'title': 'Welcome',
    })

def login(request):
    return render(request, 'core/login.html', {
        'title': 'Login',
    })
