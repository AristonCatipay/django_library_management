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
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken.')
                return redirect('core:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken.')
                return redirect('core:signup')
            else:
                # Create the user
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                # Log the user in using the credentials
                credentials = auth.authenticate(username=username, password=password)
                auth.login(request, credentials)

                return redirect('core:index')
        else:
            messages.info(request, 'Password don\'t match')
            return redirect('core:signup')

    return render(request, 'core/signup.html', {
        'title': 'Sign up',
    })