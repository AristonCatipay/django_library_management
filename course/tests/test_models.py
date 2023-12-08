from django.test import TestCase
from course.models import Course


class CourseModelTest(TestCase):

    def setUp(self):
        # Setup run before every test method.
        self.course1 = Course.objects.create(name='Test Course 1', description='Test Description 1')
        self.course2 = Course.objects.create(name='Test Course 2', description='Test Description 2')

    def tearDown(self):
        # Clean up run after every test method.
        self.course1.delete()
        self.course2.delete()

    def test_course_creation(self):
        # Test the course creation.
        self.assertEqual(self.course1.name, 'Test Course 1')
        self.assertEqual(self.course1.description, 'Test Description 1')
        self.assertEqual(self.course2.name, 'Test Course 2')
        self.assertEqual(self.course2.description, 'Test Description 2')

# You can add more test methods as needed
