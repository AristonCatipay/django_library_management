from django.test import TestCase
from django.urls import reverse, resolve
from thesis.views import view_thesis, add, view_thesis_detail, edit, add_author, add_author_in_author_list
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
        self.assertEquals(resolve(url).func, view_thesis)

    def test_add_url(self):
        url = reverse('thesis:add')
        self.assertEquals(resolve(url).func, add)
    
    def test_detail_url(self):
        url = reverse('thesis:detail', args=[self.thesis.pk])
        self.assertEquals(resolve(url).func, view_thesis_detail)

    def test_edit_url(self):
        url = reverse('thesis:edit', args=[self.thesis.pk])
        self.assertEquals(resolve(url).func, edit)

    def test_add_author_url(self):
        url = reverse('thesis:add_author')
        self.assertEquals(resolve(url).func, add_author)

    def test_add_author_in_author_list_url(self):
        url = reverse('thesis:add_author_in_author_list', args=[self.author.pk])
        self.assertEquals(resolve(url).func, add_author_in_author_list)

    def tearDown(self):
        self.thesis.delete()
        self.author.delete()
        self.course.delete()
