from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import FileResponse, Http404
from course.models import Course
from .models import Thesis, Author_List
from .forms import ThesisForm, AuthorForm, AuthorListForm

def index(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'is_staff': is_staff,
        'theses': theses,
        'courses': courses,
    })

def detail(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

    thesis = get_object_or_404(Thesis, pk=primary_key)
    authors = Author_List.objects.filter(thesis_id=primary_key)
    
    return render(request, 'thesis/detail.html', {
        'title': 'Thesis Detail',
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
    is_staff = True if request.user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thesis:index')
    else:
        form = ThesisForm()
    return render(request, 'thesis/form.html', {
        'title': 'Thesis',
        'form': form,
        'is_staff': is_staff,
    })

def edit(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'form': form,
        'is_staff': is_staff,
    })

def add_author(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'form': form,
        'is_staff': is_staff,
    })

def add_author_in_author_list(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'form': form,
        'is_staff': is_staff,
    })