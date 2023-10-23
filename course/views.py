from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def index(request):
    courses = Course.objects.all()

    return render(request, 'course/index.html', {
        'title': 'Course',
        'courses': courses,
    })

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
        'form': form,
    })
