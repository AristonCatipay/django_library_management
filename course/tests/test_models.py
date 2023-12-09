from django.test import TestCase
from course.models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Test Course', abbreviation='TC')

    def tearDown(self):
        self.course.delete()

    def test_course_name_content(self):
        expected_course_name = f'{self.course.name}'
        self.assertEqual(expected_course_name, 'Test Course')

    def test_course_abbreviation_content(self):
        expected_course_abbreviation = f'{self.course.abbreviation}'
        self.assertEqual(expected_course_abbreviation, 'TC')
