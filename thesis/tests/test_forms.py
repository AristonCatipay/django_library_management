from django.test import TestCase
from thesis.forms import ThesisForm, AuthorForm, AuthorListForm
from course.models import Course
from thesis.models import Author

class ThesisTestForm(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.author = Author.objects.create(
            name='Author test',
            first_name='Firstname test',
            last_name='Lastname test',
            course=self.course,
        )

    def tearDown(self):
        self.author.delete()
        self.course.delete()

    def test_thesis_form_fields(self):
        form = ThesisForm()
        expected_fields = ['title', 'date_published', 'course', 'image', 'file']
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_thesis_form(self):
        form = ThesisForm(data={
            'title': 'Thesis title test',
            'date_published': '2023-03-03',
            'course' : self.course.pk,  
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())

    def test_author_form_fields(self):
        form = AuthorForm()
        expected_fields = ['first_name', 'last_name', 'image', 'course']
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_author_form(self):
        form = AuthorForm(data={
            'first_name': 'Firstname test',
            'last_name': 'Lastname test',
            'course' : self.course.pk,  
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())