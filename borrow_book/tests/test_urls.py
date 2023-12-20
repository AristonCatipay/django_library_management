from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from borrow_book.views import read_borrow_book_transactions, create_request_to_borrow_book, read_requests_to_borrow_book, approve_borrow_book_request, read_books_for_pick_up, approve_book_pick_up, read_books_for_return, book_return_approved
from borrow_book.models import Borrow_Book
from book.models import Book, Author
from course.models import Course
from user_profile.models import Profile

class BorrowBookTestUrls(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.user_staff = User.objects.create_user(
            first_name = 'firstname staff',
            last_name = 'lastname staff',
            username='testuser staff',
            email='emailtest staff',
            password='12345'
        )
        self.group_staff = Group.objects.create(name='staff')
        self.course = Course.objects.create(name='Not specified', abbreviation='NS')
        self.user_staff_profile = Profile.objects.create(user=self.user_staff, course=self.course)
        self.user_staff.groups.add(self.group_staff)

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

        self.borrow_book = Borrow_Book.objects.create(
            created_by = self.user,
            book = self.book,
        )

    def test_read_borrow_book_transactions_url(self):
        url = reverse('borrow_book:read_borrow_book_transactions')
        self.assertEquals(resolve(url).func, read_borrow_book_transactions)

    def test_create_request_to_borrow_book_url(self):
        url = reverse('borrow_book:create_request_to_borrow_book', args=[self.book.pk])
        self.assertEquals(resolve(url).func, create_request_to_borrow_book)

    def test_read_requests_to_borrow_book_url(self):
        url = reverse('borrow_book:read_requests_to_borrow_book')
        self.assertEquals(resolve(url).func, read_requests_to_borrow_book)

    def test_approve_borrow_book_request_url(self):
        url = reverse('borrow_book:approve_borrow_book_request', args=[self.borrow_book.pk])
        self.assertEquals(resolve(url).func, approve_borrow_book_request)

    def test_read_books_for_pick_up_url(self):
        url = reverse('borrow_book:read_books_for_pick_up')
        self.assertEquals(resolve(url).func, read_books_for_pick_up)

    def test_approve_book_pick_up_url(self):
        url = reverse('borrow_book:approve_book_pick_up', args=[self.borrow_book.pk])
        self.assertEquals(resolve(url).func, approve_book_pick_up)

    def test_read_books_for_return_url(self):
        url = reverse('borrow_book:read_books_for_return')
        self.assertEquals(resolve(url).func, read_books_for_return)

    def test_book_return_approved_url(self):
        url = reverse('borrow_book:book_return_approved', args=[self.borrow_book.pk])
        self.assertEquals(resolve(url).func, book_return_approved)

    def tearDown(self):
        self.borrow_book.delete()
        self.book.delete()
        self.author.delete()
        self.course.delete()
        self.group_staff.delete()
        self.user_staff_profile.delete()
        self.user_staff.delete()
        self.user.delete()
