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
    
    def test_first_name_content(self):
        expected_value = f'{self.author.first_name}'
        self.assertTrue(expected_value, 'Test firstname')

    def test_last_name_content(self):
        expected_value = f'{self.author.last_name}'
        self.assertTrue(expected_value, 'Test lastname')

    def test_name_content(self):
        expected_value = f'{self.author.name}'
        self.assertTrue(expected_value, 'Test fullname')

    def test_course_content(self):
        course = self.author.course
        self.assertTrue(course.name, 'Not specified')