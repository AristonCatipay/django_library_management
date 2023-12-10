from django.test import TestCase
from suggestion.form import SuggestionForm

class SuggestionTestForm(TestCase):
    def test_suggestion_form(self):
        form = SuggestionForm(data={
            'book_title': 'Book Title Test',
            'comment': 'I love this book title test'
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())