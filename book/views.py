from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import BookForm, AuthorForm, AuthorListForm
from .models import Book, Author_List
from core.decorators import allow_certain_groups
from review.models import Reviewed_Item

@login_required()
def read_book(request):
    books = Book.objects.all()

    query = request.GET.get('query', '')
    if query: 
        books = Book.objects.filter(Q(title__icontains=query) | Q(isbn_number__icontains=query))
    return render(request, 'book/view_book.html', {
        'title': 'Book',
        'books': books,
        'is_staff': request.is_staff,
    })

@login_required()
def view_book_detail(request, book_primary_key):
    book = get_object_or_404(Book, pk=book_primary_key)
    authors = Author_List.objects.filter(book_id=book_primary_key)
    book_reviews = Reviewed_Item.objects.filter(book_id=book_primary_key)
    return render(request, 'book/view_book_detail.html', {
        'title': 'Book Detail',
        'is_staff': request.is_staff,
        'book': book,
        'authors': authors,
        'book_reviews': book_reviews,
    })

@login_required()
@allow_certain_groups(allowed_groups=['staff'])
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! The book has been added.')
            return redirect('book:read_book')
    else:
        form = BookForm()
    return render(request, 'book/form.html', {
        'title': 'Add Book',
        'form': form,
        'is_staff': request.is_staff,
    })

@login_required()
@allow_certain_groups(allowed_groups=['staff'])
def edit(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! The book has been edited.')
            return redirect('book:view_book_detail', primary_key=primary_key)
    else:
        form = BookForm(instance=book)

    return render(request, 'book/form.html', {
        'title': 'Edit Book',
        'form': form,
        'is_staff': request.is_staff,
    })

@login_required()
@allow_certain_groups(allowed_groups=['staff'])
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.name = f"{request.POST['first_name'].capitalize()}  {request.POST['last_name'].capitalize()}"
            author.save()
            messages.success(request, 'Success! The author has been added.')
            return redirect('book:read_book')
    else:
        form = AuthorForm()
    return render(request, 'book/form.html', {
        'title': 'Add Author',
        'form': form,
        'is_staff': request.is_staff,
    })

@login_required()
@allow_certain_groups(allowed_groups=['staff'])
def add_author_in_author_list(request, primary_key):
    if request.method == 'POST':
        form = AuthorListForm(request.POST)
        if form.is_valid():
            author_list = form.save(commit=False)
            author_list.book_id = primary_key
            author_list.save()
            messages.success(request, 'Success! The author has been added to the author list.')
            return redirect('book:read_book')
    else:
        form = AuthorListForm()

    return render(request, 'book/form.html', {
        'title': 'Add Author in Author Lists',
        'form': form,
        'is_staff': request.is_staff,
    })
