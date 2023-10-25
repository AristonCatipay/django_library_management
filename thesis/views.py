from django.contrib.auth.models import User
from django.shortcuts import render
from user_profile.models import Profile
from .models import Thesis

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
