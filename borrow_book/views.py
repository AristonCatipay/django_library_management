from django.shortcuts import render
from django.contrib.auth.models import User
from user_profile.models import Profile
from .models import Borrow_Book

def index(request):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    borrow_books = Borrow_Book.objects.filter(created_by=request.user)
    return render(request, 'borrow_book/index.html', {
        'title': 'Borrow Book', 
        'profile': profile,
        'borrow_books': borrow_books,
    })
