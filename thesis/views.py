from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import FileResponse, Http404
from user_profile.models import Profile
from course.models import Course
from .models import Thesis, Author_List
from .forms import ThesisForm, AuthorForm, AuthorListForm

def index(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    theses = Thesis.objects.all()
    courses = Course.objects.all()

    query = request.GET.get('query', '')
    course_id = request.GET.get('course', 0)

    if course_id:
        theses = Thesis.objects.filter(course=course_id)
    if query: 
        theses = Thesis.objects.filter(Q(title__icontains=query))
    return render(request, 'thesis/index.html', {
        'title': 'Thesis',
        'profile': profile,
        'is_staff': is_staff,
        'theses': theses,
        'courses': courses,
    })

def detail(request, primary_key):
    # Get user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    thesis = get_object_or_404(Thesis, pk=primary_key)
    authors = Author_List.objects.filter(thesis_id=primary_key)
    
    return render(request, 'thesis/detail.html', {
        'title': 'Thesis Detail',
        'profile': profile,
        'thesis': thesis,
        'authors': authors,
        'is_staff': is_staff,
    })

def view_file(request, file_location):
    try:
        return FileResponse(open(file_location, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    

def add(request):
    # Get the user profile.
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thesis:index')
    else:
        form = ThesisForm()
    return render(request, 'thesis/form.html', {
        'title': 'Thesis',
        'profile': profile,
        'form': form,
        'is_staff': is_staff,
    })

def edit(request, primary_key):
    # Get user profile 
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    thesis = get_object_or_404(Thesis, pk=primary_key)
    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES, instance=thesis)
        if form.is_valid():
            form.save()
            return redirect('thesis:detail', primary_key=primary_key)
    else:
        form = ThesisForm(instance=thesis)
    return render(request, 'thesis/form.html', {
        'title': 'Edit Thesis',
        'profile': profile,
        'form': form,
        'is_staff': is_staff,
    })

def add_author(request):
    # Get user profile
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save(commit=False)
            author.name = f"{request.POST['first_name'].capitalize()} {request.POST['last_name'].capitalize()}"
            author.save()
            return redirect('thesis:index')
    else:
        form = AuthorForm()

    return render(request, 'thesis/form.html', {
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
            author = form.save(commit=False)
            author.thesis_id = primary_key
            author.save()
            return redirect('thesis:detail', primary_key=primary_key) 
    else:
        form = AuthorListForm()
    return render(request, 'thesis/form.html', {
        'title': 'Add Author in Author List',
        'profile': profile,
        'form': form,
        'is_staff': is_staff,
    })