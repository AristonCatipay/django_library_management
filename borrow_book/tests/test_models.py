from django.test import TestCase
from django.contrib.auth.models import User
from borrow_book.models import Borrow_Book
from book.models import Book
from datetime import date

class BorrowBookTestModels(TestCase):
    def setUp(self):
        self.student = User.objects.create_user(
            first_name = 'firstname test',
            last_name = 'lastname test',
            username='testuser',
            email='emailtest',
            password='12345'
        )

        self.staff = User.objects.create_user(
            first_name = 'firstname staff',
            last_name = 'lastname staff',
            username='testuser staff',
            email='emailtest staff',
            password='12345'
        )
        self.book = Book.objects.create(
            title = 'Book title test',
            isbn_number = '1234324345',
            date_published = '2023-3-3',
            inventory = 3, 
            rack_number = 3,
            rack_level_number = 3,
        )
        self.borrow_book = Borrow_Book.objects.create(
            request_status = 'Returned',
            pick_up_date = '2023-12-06',
            return_due_date = '2023-12-09',
            returned_date = '2023-12-09',
            pending_days = 0,
            fine = 0,
            book = self.book,
            created_by = self.student,
            staff_approve = self.staff,
            staff_borrow = self.staff,
            staff_return = self.staff,
        )

    def tearDown(self):
        self.borrow_book.delete()
        self.book.delete()
        self.staff.delete()
        self.student.delete()

    def test_request_status_content(self):
        expected_status = f'{self.borrow_book.request_status}'
        self.assertEqual(expected_status, 'Returned')
    
    def test_request_created_content(self):
        current_date = date.today()
        expected_created_date = self.borrow_book.request_created.date()
        self.assertEqual(expected_created_date, current_date)

    def test_pick_up_date_content(self):
        expected_date = f'{self.borrow_book.pick_up_date}'
        self.assertEqual(expected_date, '2023-12-06')
    
    def test_return_due_date_content(self):
        expected_date = f'{self.borrow_book.return_due_date}'
        self.assertEqual(expected_date, '2023-12-09')

    def test_returned_date_content(self):
        expected_date = f'{self.borrow_book.returned_date}'
        self.assertEqual(expected_date, '2023-12-09')

    def test_pending_days_content(self):
        expected_value = self.borrow_book.pending_days
        self.assertEqual(expected_value, 0)

    def test_borrow_book_and_book_relationship(self):
        book = self.borrow_book.book
        self.assertEqual(book.title, 'Book title test')

    def test_borrow_book_and_created_by_user_relationship(self):
        student = self.borrow_book.created_by
        self.assertEqual(student.username, 'testuser')

    def test_borrow_book_and_staff_approve_relationship(self):
        staff = self.borrow_book.staff_approve
        self.assertEqual(staff.username, 'testuser staff')

    def test_borrow_book_and_staff_borrow_relationship(self):
        staff = self.borrow_book.staff_borrow
        self.assertEqual(staff.username, 'testuser staff')

    def test_borrow_book_and_staff_return_relationship(self):
        staff = self.borrow_book.staff_return
        self.assertEqual(staff.username, 'testuser staff')