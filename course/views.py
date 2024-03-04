from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from core.decorators import allow_certain_groups
from .models import Course
from .forms import CourseForm

@login_required
def view_course(request):
    courses = Course.objects.all()
    return render(request, 'course/course.html', {
        'title': 'Course',
        'is_staff': request.is_staff,
        'courses': courses,
    })

@login_required
@allow_certain_groups(['staff'])
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! The course has been successfully added!')
            return redirect('course:view_course')
        else:
            messages.error(request, 'Oops! Something went wrong while trying to add the course.')
    else:
        form = CourseForm()
    return render(request, 'course/form.html', {
        'title': 'Add Course',
        'is_staff': request.is_staff,
        'form': form,
    })

@login_required
@allow_certain_groups(['staff'])
def update_course(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! The course has been successfully edited!')
            return redirect('course:view_course')
        else:
            messages.error(request, 'Oops! Something went wrong while trying to edit the course.')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course/form.html', {
        'title': 'Edit Course',
        'is_staff': request.is_staff,
        'form': form,
    })

@login_required
@allow_certain_groups(['staff'])
def delete_course(request, primary_key):
    course = get_object_or_404(Course, pk=primary_key)
    course.delete()
    messages.success(request, 'Success! The course has been successfully deleted!')
    return redirect('course:view_course')
