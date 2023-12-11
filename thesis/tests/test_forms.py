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