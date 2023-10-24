from django.shortcuts import render

def index(request):
    return render(request, 'book/index.html', {
        'title': 'Book',
    })

def add(request):
    return render(request, 'book/form.html', {
        'title': 'Add Book',
    })
