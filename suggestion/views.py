from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_profile.models import Profile
from .models import Suggestion

def index(request):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    suggestions = Suggestion.objects.all()
    return render(request, 'suggestion/index.html', {
        'title': 'Suggestion',
        'profile': profile,
        'suggestions': suggestions,
    })