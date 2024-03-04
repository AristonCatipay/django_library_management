from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BookReviewForm
from .models import Reviewed_Item
from book.models import Book

@login_required
def create_review(request, book_id):
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
            messages.success(request, 'Success! The review has been added.')
            return redirect('borrow_book:index')
    else:
        form = BookReviewForm()
    return render(request, 'review/form.html', {
        'title': 'Add Review',
        'is_staff': request.is_staff,
        'form': form,
    })