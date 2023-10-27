from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from user_profile.models import Profile
from .models import Suggestion
from .form import SuggestionForm

def index(request):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    suggestions = Suggestion.objects.filter(created_by=request.user)
    return render(request, 'suggestion/index.html', {
        'title': 'Suggestion',
        'profile': profile,
        'suggestions': suggestions,
    })

def add(request):
    # Get user profile
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.created_by = request.user
            suggestion.save()
            return redirect('suggestion:index')
    else:
        form = SuggestionForm()
    return render(request, 'suggestion/form.html', {
        'title': 'Add Suggestion',
        'profile': profile,
        'form': form,
    })

def edit(request, primary_key):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    suggestion = get_object_or_404(Suggestion, id=primary_key)
    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            form.save()
            return redirect('suggestion:index')
    else:
        form = SuggestionForm(instance=suggestion)

    return render(request, 'suggestion/form.html', {
        'title': 'Edit Suggestion',
        'profile': profile,
        'form': form,
    })