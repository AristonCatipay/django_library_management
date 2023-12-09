from django.test import TestCase
from course.forms import CourseForm

class CourseTestForms(TestCase):
    def test_course_form(self):
        form = CourseForm(data={
            'name': 'Test Course',
            'abbreviation': 'TC'
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())
