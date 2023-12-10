from django.test import TestCase
from review.forms import BookReviewForm

class ReviewTestForms(TestCase):
    def test_book_review_form(self):
        form = BookReviewForm(data={
            'review': 'This is a review.'
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())