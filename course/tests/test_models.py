from django.test import TestCase
from course.models import Course

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Test Course', abbreviation='TC')

    def tearDown(self):
        self.course.delete()

    
