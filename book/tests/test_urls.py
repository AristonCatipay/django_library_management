from django.test import TestCase
from django.urls import reverse, resolve
from book.views import index, add, detail, edit, add_author, add_author_in_author_list
from book.models import Book, Author, Author_List

class BookTestUrls(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )

        self.author = Author.objects.create(
            name = 'Author test',
            first_name = 'Firstname test',
            last_name = 'Lastname test',
        )

    def test_index_url(self):
        url = reverse('book:index')
        self.assertEquals(resolve(url).func, index)

    def test_add_url(self):
        url = reverse('book:add')
        self.assertEquals(resolve(url).func, add)
    
    def test_detail_url(self):
        url = reverse('book:detail', args=[self.book.pk])
        self.assertEquals(resolve(url).func, detail)

    def test_edit_url(self):
        url = reverse('book:edit', args=[self.book.pk])
        self.assertEquals(resolve(url).func, edit)

    def test_add_author_url(self):
        url = reverse('book:add_author')
        self.assertEquals(resolve(url).func, add_author)

    def test_add_author_in_author_list_url(self):
        url = reverse('book:add_author_in_author_list', args=[self.author.pk])
        self.assertEquals(resolve(url).func, add_author_in_author_list)

    def tearDown(self):
        self.book.delete()
        self.author.delete()
