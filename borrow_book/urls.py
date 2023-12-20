from django.urls import path
from . import views

app_name = 'borrow_book'

urlpatterns = [
    path('transactions/read/', views.read_borrow_book_transactions, name='read_borrow_book_transactions'),
    path('borrow-request/read/', views.read_requests_to_borrow_book, name='read_requests_to_borrow_book'),
    path('borrow-request/create/<int:book_primary_key>/', views.create_request_to_borrow_book, name='create_request_to_borrow_book'),
    path('borrow-request-approve/<int:borrow_book_primary_key>/', views.approve_borrow_book_request, name='approve_borrow_book_request'),
    path('for-pickup/read/', views.read_books_for_pick_up, name='read_books_for_pick_up'),
    path('book-pick-up-approve/<int:primary_key>/', views.book_pick_up_approve, name='book_pick_up_approve'),
    path('book-return/', views.book_return, name='book_return'),
    path('book-return-approved/<int:primary_key>/', views.book_return_approved, name='book_return_approved'),
]