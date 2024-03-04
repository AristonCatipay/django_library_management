from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Suggestion
from .form import SuggestionForm

@login_required
def view_suggestion(request):
    suggestions = Suggestion.objects.filter(created_by=request.user)
    return render(request, 'suggestion/suggestion.html', {
        'title': 'Suggestion',
        'suggestions': suggestions,
        'is_staff': request.is_staff,
    })

@login_required
def add(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.created_by = request.user
            suggestion.save()
            messages.success(request, 'Success! The suggestion has been added.')
            return redirect('suggestion:view_suggestion')
    else:
        form = SuggestionForm()
    return render(request, 'suggestion/form.html', {
        'title': 'Add Suggestion',
        'form': form,
        'is_staff': request.is_staff,
    })

@login_required
def edit(request, primary_key):
    suggestion = get_object_or_404(Suggestion, id=primary_key)
    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success! The suggestion has been edited.')
            return redirect('suggestion:view_suggestion')
    else:
        form = SuggestionForm(instance=suggestion)

    return render(request, 'suggestion/form.html', {
        'title': 'Edit Suggestion',
        'form': form,
        'is_staff': request.is_staff,
    })