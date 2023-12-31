from django.test import TestCase
from book.forms import BookForm, AuthorForm, AuthorListForm
from book.models import Author

class BookTestForm(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Doe')
        
    def tearDown(self):
        self.author.delete()

    def test_book_form_fields(self):
        form = BookForm()
        expected_fields = ['title', 'cover_image', 'overview_image', 'table_of_contents_image', 'isbn_number', 'date_published', 'inventory', 'rack_number', 'rack_level_number']
        self.assertEqual(list(form.fields.keys()), expected_fields)

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

    def test_author_form_fields(self):
        form = AuthorForm()
        expected_fields = ['first_name', 'last_name', 'author_image']
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_author_form(self):
        form = AuthorForm(data={
            'first_name' : 'Firstname test',
            'last_name' : 'Lastname test',
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())

    def test_author_list_form_fields(self):
        form = AuthorListForm()
        expected_fields = ['author']
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_author_list_form(self):
        form = AuthorListForm(data={
            'author': self.author.id,
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())