from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from user_profile.models import Profile
from .models import Thesis, Author_List
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

def detail(request, primary_key):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    thesis = get_object_or_404(Thesis, pk=primary_key)
    authors = Author_List.objects.filter(thesis_id=primary_key)
    
    return render(request, 'thesis/detail.html', {
        'title': 'Thesis Detail',
        'profile': profile,
        'thesis': thesis,
        'authors': authors,
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

def edit(request, primary_key):
    # Get user profile 
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    thesis = get_object_or_404(Thesis, pk=primary_key)
    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES, instance=thesis)
        if form.is_valid():
            form.save()
            return redirect('thesis:detail', primary_key=primary_key)
    else:
        form = ThesisForm(instance=thesis)
    return render(request, 'thesis/form.html', {
        'title': 'Edit Thesis',
        'profile': profile,
        'form': form,
    })