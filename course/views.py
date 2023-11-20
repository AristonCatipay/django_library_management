from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.decorators import allow_certain_groups
from .models import Course
from .forms import CourseForm

@login_required
def index(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {
        'title': 'Course',
        'is_staff': request.is_staff,
        'courses': courses,
    })

@login_required
@allow_certain_groups(['staff'])
def add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:index')
    else:
        form = CourseForm()
    return render(request, 'course/form.html', {
        'title': 'Add Course',
        'is_staff': request.is_staff,
        'form': form,
    })

@login_required
@allow_certain_groups(['staff'])
def edit(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course:index')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/form.html', {
        'title': 'Edit Course',
        'is_staff': request.is_staff,
        'form': form,
    })

@login_required
@allow_certain_groups(['staff'])
def delete(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    course.delete()
    return redirect('course:index')
