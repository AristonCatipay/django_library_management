from django.shortcuts import render

def index(request):
    return render(request, 'thesis/index.html', {
        'title': 'Thesis',
    })
