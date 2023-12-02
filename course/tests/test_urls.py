from django.test import SimpleTestCase
from django.urls import reverse, resolve
from course.views import index, add, edit, delete

class CourseTestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('course:index')
        self.assertEquals(resolve(url).func, index)