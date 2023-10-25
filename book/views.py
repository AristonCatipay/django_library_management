from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from user_profile.models import Profile
from .form import BookForm
from .models import Book


def index(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    books = Book.objects.all()
    return render(request, 'book/index.html', {
        'title': 'Book',
        'profile': profile,
        'books': books,
    })

def detail(request, primary_key):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'book/detail.html', {
        'title': 'Book Detail',
        'profile': profile,
        'book': book,
    })


def add(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book:index')
    else:
        form = BookForm()
    return render(request, 'book/form.html', {
        'title': 'Add Book',
        'profile': profile,
        'form': form,
    })

def edit(request, primary_key):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    return render(request, 'book/detail.html', {
        'title': 'Edit Book',
        'profile': profile,
    })
