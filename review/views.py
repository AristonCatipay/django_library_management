from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import BookReviewForm
from .models import Reviewed_Item
from user_profile.models import Profile
from book.models import Book

def add(request, book_id):
    is_staff = True if request.user.groups.filter(name='staff') else False

    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            # Save the review
            review = form.save(commit=False)
            review.user = request.user
            review.profile = request.user.profile
            review.save()

            # Set the review to the book.
            book = Book.objects.get(pk=book_id)
            book_review = Reviewed_Item.objects.create(book=book, review=review)
            book_review.save()
            return redirect('borrow_book:index')
    else:
        form = BookReviewForm()
    return render(request, 'review/form.html', {
        'title': 'Add Review',
        'is_staff': is_staff,
        'form': form,
    })