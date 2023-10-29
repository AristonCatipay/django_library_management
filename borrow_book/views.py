from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
from user_profile.models import Profile
from book.models import Book
from .models import Borrow_Book
from .forms import BorrowBookRequestApproveForm, BookPickUpApproveForm


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

# This will add a book request
def add(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    is_borrowed = Borrow_Book.objects.filter(created_by=request.user, book=book).filter(~Q(request_status='Returned')).exists()
    if is_borrowed:
        return redirect('book:detail', primary_key=primary_key)
    else:
        borrow_book = Borrow_Book.objects.create(created_by=request.user, book=book)
        borrow_book.save()
        return redirect('borrow_book:index')

def borrow_request(request):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    borrow_books = Borrow_Book.objects.filter(created_by=request.user).filter(request_status='Request')
    return render(request, 'borrow_book/borrow_request.html', {
        'title': 'Borrow Request',
        'profile': profile,
        'borrow_books': borrow_books,
    })

def borrow_request_approve(request, primary_key):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    transaction = get_object_or_404(Borrow_Book, pk=primary_key)

    if request.method == 'POST':
        form = BorrowBookRequestApproveForm(request.POST, instance=transaction)
        if form.is_valid():
            approve = form.save(commit=False)
            approve.request_status = 'Approved'
            approve.staff_approve = request.user
            approve.save()
            return redirect('borrow_book:borrow_request')
    else:
        form = BorrowBookRequestApproveForm(instance=transaction)
    return render(request, 'borrow_book/form.html', {
        'title': 'Borrow Book Request Approve',
        'profile': profile,
        'form': form,
    })

def book_pick_up(request):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    borrow_books = Borrow_Book.objects.filter(created_by=request.user).filter(request_status='Approved')
    return render(request, 'borrow_book/book_pick_up.html', {
        'title': 'Borrow Request',
        'profile': profile,
        'borrow_books': borrow_books,
    })

def book_pick_up_approve(request, primary_key):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)

    transaction = get_object_or_404(Borrow_Book, pk=primary_key)

    if request.method == 'POST':
        form = BookPickUpApproveForm(request.POST, instance=transaction)
        if form.is_valid():
            approve = form.save(commit=False)
            approve.request_status = 'Borrowed'
            approve.staff_borrow = request.user
            approve.save()
            return redirect('borrow_book:borrow_request')
    else:
        form = BookPickUpApproveForm(instance=transaction)
    return render(request, 'borrow_book/form.html', {
        'title': 'Book Pick Up Approve',
        'profile': profile,
        'form': form,
    })

