from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class Borrow_Book(models.Model):
    REQUEST = 'Request' 
    BORROWED = 'Borrowed'
    PENDING = 'Pending'
    APPROVED = 'Approved'
    RETURNED = 'Returned'

    REQUEST_STATUS_CHOICES = {
        (REQUEST, 'Request'),
        (BORROWED, 'Borrowed'),
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (RETURNED, 'Returned'),
    }
    
    request_status = models.CharField(max_length=15, choices=REQUEST_STATUS_CHOICES, default=REQUEST)
    request_created = models.DateTimeField(auto_now_add=True)
    pick_up_date = models.DateField(null=True)
    return_due_date = models.DateField(null=True)
    returned_date = models.DateField(null=True)
    pending_days = models.IntegerField(null=True)
    fine = models.IntegerField(null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, related_name='created_by_id', on_delete=models.PROTECT)
    staff_approve = models.ForeignKey(User, related_name='staff_approve_id', on_delete=models.PROTECT, null=True)
    staff_borrow = models.ForeignKey(User, related_name='staff_borrow_id', on_delete=models.PROTECT, null=True)
    staff_return = models.ForeignKey(User, related_name='staff_return_id', on_delete=models.PROTECT, null=True)


