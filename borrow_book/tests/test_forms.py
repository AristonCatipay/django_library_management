from django.test import TestCase
from borrow_book.forms import BorrowBookRequestApproveForm, BookPickUpApproveForm

class BorrowBookTestForms(TestCase):
    def test_borrow_book_request_approve_form(self):
        form = BorrowBookRequestApproveForm(data={
            'pick_up_date' : '2023-12-06',
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())

    def test_book_pick_up_approve_form(self):
        form = BookPickUpApproveForm(data={
            'return_due_date' : '2023-12-09',
        })
        self.assertTrue(form.is_valid(), form.errors.as_data())