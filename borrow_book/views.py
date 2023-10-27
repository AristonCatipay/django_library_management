from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from user_profile.models import Profile
from book.models import Book
from .models import Borrow_Book


def index(request):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    borrow_books = Borrow_Book.objects.filter(created_by=request.user)
    return render(request, 'borrow_book/index.html', {
        'title': 'Borrowed Books', 
        'profile': profile,
        'borrow_books': borrow_books,
    })

def add(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    is_borrowed = Borrow_Book.objects.filter(created_by=request.user, book=book).filter(~Q(request_status='Returned')).exists()
    if is_borrowed:
        return redirect('book:detail', primary_key=primary_key)
    else:
        borrow_book = Borrow_Book.objects.create(created_by=request.user, book=book)
        borrow_book.save()
        return redirect('borrow_book:index')
