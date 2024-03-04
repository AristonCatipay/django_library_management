from django.test import TestCase
from django.urls import reverse, resolve
from course.views import view_course, add, edit, delete
from course.models import Course

class CourseTestUrls(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')

    def test_index_url(self):
        url = reverse('course:index')
        self.assertEquals(resolve(url).func, view_course)

    def test_add_url(self):
        url = reverse('course:add')
        self.assertEquals(resolve(url).func, add)

    def test_edit_url(self):
        url = reverse('course:edit', args=[self.course.pk])
        self.assertEquals(resolve(url).func, edit)
    
    def test_delete_url(self):
        url = reverse('course:delete', args=[self.course.pk])
        self.assertEquals(resolve(url).func, delete)

    def tearDown(self):
        self.course.delete()