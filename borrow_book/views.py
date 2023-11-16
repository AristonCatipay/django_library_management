from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from book.models import Book
from .models import Borrow_Book
from .forms import BorrowBookRequestApproveForm, BookPickUpApproveForm
from datetime import date

def index(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    borrow_books = Borrow_Book.objects.filter(created_by=request.user)
    return render(request, 'borrow_book/index.html', {
        'title': 'Borrowed Books',
        'borrow_books': borrow_books,
        'is_staff': is_staff,
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
    is_staff = True if request.user.groups.filter(name='staff') else False

    borrow_books = Borrow_Book.objects.filter(created_by=request.user).filter(request_status='Request')
    return render(request, 'borrow_book/borrow_request.html', {
        'title': 'Borrow Request',
        'borrow_books': borrow_books,
        'is_staff': is_staff,
    })

def borrow_request_approve(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'is_staff': is_staff,
        'form': form,
    })

def book_pick_up(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    borrow_books = Borrow_Book.objects.filter(created_by=request.user).filter(request_status='Approved')
    return render(request, 'borrow_book/book_pick_up.html', {
        'title': 'Borrow Request',
        'borrow_books': borrow_books,
        'is_staff': is_staff,
    })

def book_pick_up_approve(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'form': form,
        'is_staff': is_staff,
    })

def book_return(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    borrow_books = Borrow_Book.objects.filter(created_by=request.user).filter(request_status='Borrowed')
    return render(request, 'borrow_book/return_book.html', {
        'title': 'Borrow Request',
        'borrow_books': borrow_books,
        'is_staff': is_staff,
    })

def book_return_approved(request, primary_key):
    transaction = get_object_or_404(Borrow_Book, pk=primary_key)

    transaction.request_status = 'Returned'
    transaction.staff_return = request.user
    transaction.returned_date = date.today()
    delta = transaction.returned_date - transaction.return_due_date
    if delta.days > 0:
        transaction.pending_days = delta.days
        transaction.fine = transaction.pending_days * 20
        transaction.save()
        return redirect('borrow_book:borrow_request')
    else:
        transaction.pending_days = 0
        transaction.fine = 0
        transaction.save()
        return redirect('borrow_book:borrow_request')
