from django.test import TestCase
from django.urls import reverse, resolve
from review.views import create_review
from book.models import Book

class ReviewTestUrls(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

    def test_add_url(self):
        url = reverse('review:add', args=[self.book.pk])
        self.assertEquals(resolve(url).func, create_review)

    def tearDown(self):
        self.book.delete()