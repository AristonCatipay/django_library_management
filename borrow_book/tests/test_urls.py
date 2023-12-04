from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from borrow_book.views import index, add, borrow_request, borrow_request_approve, book_pick_up, book_pick_up_approve, book_return, book_return_approved
from borrow_book.models import Borrow_Book
from book.models import Book, Author
from course.models import Course
from user_profile.models import Profile

class BookTestUrls(TestCase):
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

    def tearDown(self):
        self.borrow_book.delete()
        self.book.delete()
        self.author.delete()
        self.course.delete()
        self.group_staff.delete()
        self.user_staff_profile.delete()
        self.user_staff.delete()
        self.user.delete()
