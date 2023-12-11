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

class ThesisTestModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.thesis = Thesis.objects.create(
            title='Thesis title test',
            date_published='2023-03-03',
            course=self.course,
        )

    def tearDown(self):
        self.thesis.delete()
        self.course.delete()

    def test_title_content(self):
        expected_value = f'{self.thesis.title}'
        self.assertTrue(expected_value, 'Thesis title test')

    def test_date_published_content(self):
        expected_value = f'{self.thesis.date_published}'
        self.assertTrue(expected_value, '2023-03-03')

    def test_course_content(self):
        course = self.thesis.course
        self.assertTrue(course.name, 'Not specified')

class AuthorListTestModel(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.thesis = Thesis.objects.create(
            title='Thesis title test',
            date_published='2023-3-3',
            course=self.course,
        )

        self.author = Author.objects.create(
            name='Author test',
            first_name='Firstname test',
            last_name='Lastname test',
            course=self.course,
        )
        
        self.author_list = Author_List.objects.create(
            thesis=self.thesis,
            author=self.author,
        )

    def tearDown(self):
        self.author_list.delete()
        self.author.delete()
        self.thesis.delete()
        self.course.delete()

    def test_thesis_content(self):
        thesis = self.author_list.thesis
        self.assertEqual(thesis.title, 'Thesis title test')

    def test_author_content(self):
        author = self.author_list.author
        self.assertEqual(author.name, 'Author test')