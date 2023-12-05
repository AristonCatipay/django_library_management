from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from borrow_book.views import index, add, borrow_request, borrow_request_approve, book_pick_up, book_pick_up_approve, book_return, book_return_approved
from borrow_book.models import Borrow_Book
from book.models import Book, Author
from course.models import Course
from user_profile.models import Profile

class BorrowBookTestView(TestCase):
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

    def test_index_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/index.html')

    def test_add_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:add', kwargs={'primary_key': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        data = {
            'created_by': self.user.pk,
            'book': self.book.pk,
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Add Borrow Request):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def test_borrow_request_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:borrow_request')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/borrow_request.html')

    def test_book_pick_up_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:book_pick_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/book_pick_up.html')

    def test_book_return_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:book_return')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/return_book.html')

    def tearDown(self):
        self.borrow_book.delete()
        related_borrow_book_transaction = Borrow_Book.objects.filter(book=self.book)
        related_borrow_book_transaction.delete()
        self.book.delete()
        self.author.delete()
        self.course.delete()
        self.group_staff.delete()
        self.user_staff_profile.delete()
        self.user_staff.delete()
        self.user.delete()
