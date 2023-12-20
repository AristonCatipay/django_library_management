from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from book.models import Book
from core.decorators import allow_certain_groups
from .models import Borrow_Book
from .forms import BorrowBookRequestApproveForm, BookPickUpApproveForm

@login_required()
def read_borrow_book_transactions(request):
    borrow_books = Borrow_Book.objects.filter(created_by=request.user)
    return render(request, 'borrow_book/index.html', {
        'title': 'Borrowed Books',
        'borrow_books': borrow_books,
        'is_staff': request.is_staff,
    })
    
@login_required()
@allow_certain_groups(['staff'])
def read_requests_to_borrow_book(request):
    borrow_books = Borrow_Book.objects.filter(request_status='Request')
    return render(request, 'borrow_book/borrow_request.html', {
        'title': 'Borrow Request',
        'borrow_books': borrow_books,
        'is_staff': request.is_staff,
    })

@login_required()
def create_request_to_borrow_book(request, book_primary_key):
    book = get_object_or_404(Book, pk=book_primary_key)
    is_borrowed = Borrow_Book.objects.filter(created_by=request.user, book=book).filter(~Q(request_status='Returned')).exists()
    if is_borrowed:
        return redirect('book:detail', primary_key=book_primary_key)
    else:
        borrow_book = Borrow_Book.objects.create(created_by=request.user, book=book)
        borrow_book.save()
        return redirect('borrow_book:read_borrow_book_transactions')

@login_required()
@allow_certain_groups(['staff'])
def approve_borrow_book_request(request, borrow_book_primary_key):
    transaction = get_object_or_404(Borrow_Book, pk=borrow_book_primary_key)

    if request.method == 'POST':
        form = BorrowBookRequestApproveForm(request.POST, instance=transaction)
        if form.is_valid():
            approve = form.save(commit=False)
            approve.request_status = 'Approved'
            approve.staff_approve = request.user
            approve.save()
            return redirect('borrow_book:read_requests_to_borrow_book')
    else:
        form = BorrowBookRequestApproveForm(instance=transaction)
    return render(request, 'borrow_book/form.html', {
        'title': 'Borrow Book Request Approve',
        'is_staff': request.is_staff,
        'form': form,
    })

@login_required()
@allow_certain_groups(['staff'])
def read_books_for_pick_up(request):
    borrow_books = Borrow_Book.objects.filter(request_status='Approved')
    return render(request, 'borrow_book/book_pick_up.html', {
        'title': 'Borrow Request',
        'borrow_books': borrow_books,
        'is_staff': request.is_staff,
    })

@login_required()
@allow_certain_groups(['staff'])
def approve_book_pick_up(request, borrow_book_primary_key):
    transaction = get_object_or_404(Borrow_Book, pk=borrow_book_primary_key)

    if request.method == 'POST':
        form = BookPickUpApproveForm(request.POST, instance=transaction)
        if form.is_valid():
            approve = form.save(commit=False)
            approve.request_status = 'Borrowed'
            approve.staff_borrow = request.user
            approve.save()
            return redirect('borrow_book:read_requests_to_borrow_book')
    else:
        form = BookPickUpApproveForm(instance=transaction)
    return render(request, 'borrow_book/form.html', {
        'title': 'Book Pick Up Approve',
        'form': form,
        'is_staff': request.is_staff,
    })

@login_required()
@allow_certain_groups(['staff'])
def book_return(request):
    borrow_books = Borrow_Book.objects.filter(request_status='Borrowed')
    return render(request, 'borrow_book/return_book.html', {
        'title': 'Borrow Request',
        'borrow_books': borrow_books,
        'is_staff': request.is_staff,
    })

@login_required()
@allow_certain_groups(['staff'])
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
        return redirect('borrow_book:read_requests_to_borrow_book')
    else:
        transaction.pending_days = 0
        transaction.fine = 0
        transaction.save()
        return redirect('borrow_book:read_requests_to_borrow_book')
