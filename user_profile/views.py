from django.shortcuts import render
from django.contrib.auth import get_user_model
from . models import Profile

User = get_user_model()

def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    return render(request, 'user_profile/index.html', {
        'title': 'Profile',
        'profile': profile,
    })