from django.test import TestCase
from django.urls import reverse, resolve
from thesis.views import index, add, detail, edit, add_author, add_author_in_author_list
from thesis.models import Thesis, Author
from course.models import Course

class ThesisTestUrls(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')

        self.thesis = Thesis.objects.create(
            title = 'Thesis title test',
            date_published = '2023-3-3',
            course = self.course,
        )

        self.author = Author.objects.create(
            name = 'Author test',
            first_name = 'Firstname test',
            last_name = 'Lastname test',
            course = self.course,
        )

    def test_index_url(self):
        url = reverse('thesis:index')
        self.assertEquals(resolve(url).func, index)

    def test_add_url(self):
        url = reverse('thesis:add')
        self.assertEquals(resolve(url).func, add)
    
    def test_detail_url(self):
        url = reverse('thesis:detail', args=[self.thesis.pk])
        self.assertEquals(resolve(url).func, detail)

    def tearDown(self):
        self.thesis.delete()
        self.author.delete()
        self.course.delete()
