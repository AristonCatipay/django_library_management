from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from user_profile.models import Profile
from .models import Course
from .forms import CourseForm

def index(request):
    is_staff = True if request.user.groups.filter(name='staff') else False
    courses = Course.objects.all()

    return render(request, 'course/index.html', {
        'title': 'Course',
        'is_staff': is_staff,
        'courses': courses,
    })

def add(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:index')
    else:
        form = CourseForm()
    return render(request, 'course/form.html', {
        'title': 'Add Course',
        'is_staff': is_staff,
        'form': form,
    })

def edit(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

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
        'is_staff': is_staff,
        'form': form,
    })

def delete(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    course.delete()
    return redirect('course:index')
