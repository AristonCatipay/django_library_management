from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from user_profile.models import Profile
from .forms import BookForm, AuthorForm, AuthorListForm
from .models import Book, Author_List


def index(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    books = Book.objects.all()
    return render(request, 'book/index.html', {
        'title': 'Book',
        'profile': profile,
        'books': books,
        'is_staff': is_staff,
    })

def detail(request, primary_key):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    book = get_object_or_404(Book, pk=primary_key)
    authors = Author_List.objects.filter(book_id=primary_key)
    return render(request, 'book/detail.html', {
        'title': 'Book Detail',
        'profile': profile,
        'book': book,
        'authors': authors,
        'is_staff': is_staff,
    })


def add(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

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
        'is_staff': is_staff,
    })

def edit(request, primary_key):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    book = get_object_or_404(Book, pk=primary_key)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book:detail', primary_key=primary_key)
    else:
        form = BookForm(instance=book)

    return render(request, 'book/form.html', {
        'title': 'Edit Book',
        'profile': profile,
        'form': form,
        'is_staff': is_staff,
    })

def add_author(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.name = f"{request.POST['first_name'].capitalize()}  {request.POST['last_name'].capitalize()}"
            author.save()
            return redirect('book:index')
    else:
        form = AuthorForm()
    return render(request, 'book/form.html', {
        'title': 'Add Author',
        'profile': profile,
        'form': form,
        'is_staff': is_staff,
    })

def add_author_in_author_list(request, primary_key):
     # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = AuthorListForm(request.POST)
        if form.is_valid():
            author_list = form.save(commit=False)
            author_list.book_id = primary_key
            author_list.save()
            return redirect('book:index')
    else:
        form = AuthorListForm()

    return render(request, 'book/form.html', {
        'title': 'Add Author in Author Lists',
        'profile': profile,
        'form': form,
        'is_staff': is_staff,
    })
