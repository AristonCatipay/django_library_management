from django.test import TestCase
from book.forms import BookForm, AuthorForm, AuthorListForm

class BookTestForm(TestCase):
    def test_book_form(self):
        form = BookForm(data={
            'title' : 'Book title test',
            'isbn_number' : '1234324345',
            'date_published': '2023-3-3',
            'inventory': 3,
            'rack_number': 3,
            'rack_level_number': 3,
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())

    def test_author_form(self):
        form = AuthorForm(data={
            'first_name' : 'Firstname test',
            'last_name' : 'Lastname test',
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())