from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from user_profile.models import Profile
from .models import Course
from .forms import CourseForm

def index(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False
    courses = Course.objects.all()

    return render(request, 'course/index.html', {
        'title': 'Course',
        'profile': profile,
        'is_staff': is_staff,
        'courses': courses,
    })

def add(request):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course:index')
    else:
        form = CourseForm()
    return render(request, 'course/form.html', {
        'title': 'Add Course',
        'profile': profile,
        'is_staff': is_staff,
        'form': form,
    })

def edit(request, primary_key):
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=user)
    is_staff = True if user.groups.filter(name='staff') else False

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
        'profile': profile,
        'is_staff': is_staff,
        'form': form,
    })

def delete(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    course.delete()
    return redirect('course:index')
