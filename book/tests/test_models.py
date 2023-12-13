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

    def test_inventory_content(self):
        expected_value = f'{self.book.inventory}'
        self.assertTrue(expected_value, 3)
    
    def test_rack_number_content(self):
        expected_value = f'{self.book.rack_number}'
        self.assertTrue(expected_value, 3)
    
    def test_rack_level_number_content(self):
        expected_value = f'{self.book.rack_level_number}'
        self.assertTrue(expected_value, 3)


class AuthorListTestModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

        self.author = Author.objects.create(
            name = 'Author test',
            first_name = 'Firstname test',
            last_name = 'Lastname test',
        )
        
        self.author_list = Author_List.objects.create(
            book = self.book,
            author = self.author,
        )

    def tearDown(self):
        self.author_list.delete()
        self.author.delete()
        self.book.delete()

    def test_book_content(self):
        book = self.author_list.book
        self.assertEqual(book.title, 'Book title test')

    def test_author_content(self):
        author = self.author_list.author
        self.assertEqual(author.name, 'Author test')