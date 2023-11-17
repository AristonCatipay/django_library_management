from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Suggestion
from .form import SuggestionForm

@login_required
def index(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    suggestions = Suggestion.objects.filter(created_by=request.user)
    return render(request, 'suggestion/index.html', {
        'title': 'Suggestion',
        'suggestions': suggestions,
        'is_staff': is_staff,
    })

@login_required
def add(request):
    is_staff = True if request.user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.created_by = request.user
            suggestion.save()
            return redirect('suggestion:index')
    else:
        form = SuggestionForm()
    return render(request, 'suggestion/form.html', {
        'title': 'Add Suggestion',
        'form': form,
        'is_staff': is_staff,
    })

@login_required
def edit(request, primary_key):
    is_staff = True if request.user.groups.filter(name='staff') else False

    suggestion = get_object_or_404(Suggestion, id=primary_key)
    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            form.save()
            return redirect('suggestion:index')
    else:
        form = SuggestionForm(instance=suggestion)

    return render(request, 'suggestion/form.html', {
        'title': 'Edit Suggestion',
        'form': form,
        'is_staff': is_staff,
    })