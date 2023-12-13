from django.test import TestCase
from book.models import Book, Author, Author_List

class AuthorTestModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name = 'Test firstname',
            last_name = 'Test lastname',
            name = 'Test fullname',
        )
    def tearDown(self):
        self.author.delete()
    
    def test_first_name_content(self):
        expected_value = f'{self.author.first_name}'
        self.assertTrue(expected_value, 'Test firstname')

    def test_last_name_content(self):
        expected_value = f'{self.author.last_name}'
        self.assertTrue(expected_value, 'Test lastname')

    def test_name_content(self):
        expected_value = f'{self.author.name}'
        self.assertTrue(expected_value, 'Test fullname')


class BookTestModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-03-03',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

    def tearDown(self):
        self.book.delete()

    def test_title_content(self):
        expected_value = f'{self.book.title}'
        self.assertTrue(expected_value, 'Book title test')

    def test_isbn_number_content(self):
        expected_value = f'{self.book.isbn_number}'
        self.assertTrue(expected_value, '1234324345')

    def test_date_published_content(self):
        expected_value = f'{self.book.date_published}'
        self.assertTrue(expected_value, '2023-03-03')
