from django.shortcuts import render
from .models import Course
from .forms import CourseForm

def index(request):
    courses = Course.objects.all()

    return render(request, 'course/index.html', {
        'title': 'Course',
        'courses': courses,
    })

def edit(request):
    if request.method == 'POST':
        form = CourseForm
    else:
        form = CourseForm
    return render(request, 'course/form.html', {
        'title': 'Edit Course',
        'form': form,
    })
