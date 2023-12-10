from django.test import TestCase
from thesis.models import Author, Thesis, Author_List
from course.models import Course

class AuthorTestModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.author = Author.objects.create(
            first_name = 'Test firstname',
            last_name = 'Test lastname',
            name = 'Test fullname',
            course = self.course,
        )
    def tearDown(self):
        self.author.delete()
        self.course.delete()