from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user_profile.models import Profile
from .models import Thesis
from .forms import ThesisForm

def index(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    theses = Thesis.objects.all()
    return render(request, 'thesis/index.html', {
        'title': 'Thesis',
        'profile': profile,
        'theses': theses,
    })

def add(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thesis:index')
    else:
        form = ThesisForm()
    return render(request, 'thesis/form.html', {
        'title': 'Thesis',
        'profile': profile,
        'form': form,
    })