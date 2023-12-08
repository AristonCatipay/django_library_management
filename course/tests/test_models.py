from django.test import TestCase
from course.models import Course


class CourseModelTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(name='Test Course', description='Test Description')

    def test_course_creation(self):
        self.assertTrue(isinstance(self.course, Course))
        self.assertEqual(self.course.__str__(), self.course.name)

    def test_course_str_representation(self):
        self.assertEqual(str(self.course), 'Test Course')
