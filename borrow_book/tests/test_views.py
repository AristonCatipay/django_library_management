from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, Group
from borrow_book.views import read_borrow_book_transactions, create_request_to_borrow_book, read_requests_to_borrow_book, approve_borrow_book_request, read_books_for_pick_up, approve_book_pick_up, read_books_for_return, return_book
from borrow_book.models import Borrow_Book
from book.models import Book, Author
from course.models import Course
from user_profile.models import Profile
from datetime import date

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
            return_due_date=date(2023, 4, 2)
        )

    def test_read_borrow_book_transactions_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:read_borrow_book_transactions')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/index.html')

    def test_create_request_to_borrow_book_views(self):
        self.client.force_login(self.user)
        url = reverse('borrow_book:create_request_to_borrow_book', kwargs={'book_primary_key': self.book.pk})
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

    def test_read_requests_to_borrow_book_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:read_requests_to_borrow_book')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/borrow_request.html')

    def test_approve_borrow_book_request_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:approve_borrow_book_request', kwargs={'borrow_book_primary_key':self.borrow_book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/form.html')

        data = {
            'pick_up_date': '2023-03-30',
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Approve Borrow Request):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def test_read_books_for_pick_up_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:read_books_for_pick_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/book_pick_up.html')
    
    def test_approve_book_pick_up_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:approve_book_pick_up', kwargs={'borrow_book_primary_key':self.borrow_book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/form.html')

        data = {
            'return_due_date': '2023-04-02',
        }

        response = self.client.post(url, data)
        print("\nTest Data Used (Approve Borrow Pickup):", data, "\n")

        if response.context:
            # Retrieve form instance to access errors
            form = response.context['form']
            if form.errors:
                print(form.errors)
        self.assertEqual(response.status_code, 302)

    def test_read_books_for_return_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:read_books_for_return')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'borrow_book/return_book.html')

    def test_return_book_views(self):
        self.client.force_login(self.user_staff)
        url = reverse('borrow_book:return_book', kwargs={'borrow_book_primary_key':self.borrow_book.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)

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
