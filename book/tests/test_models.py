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