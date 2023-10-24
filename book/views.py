from django.shortcuts import render, redirect
from .form import BookForm
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {
        'title': 'Book',
        'books': books,
    })

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book:index')
    else:
        form = BookForm()
    return render(request, 'book/form.html', {
        'title': 'Add Book',
        'form': form,
    })

def edit(request):
    return render(request, 'book/detail.html', {
        'title': 'Edit Book'
    })
