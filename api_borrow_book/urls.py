from django.urls import path
from . import views

urlpatterns = [
    path('transactions/read/', views.read_borrow_book_transactions),
    path('borrow-request/read/', views.read_requests_to_borrow_book),
    path('borrow-request/create/<int:book_primary_key>/', views.create_request_to_borrow_book),
    path('borrow-request/approve/<int:borrow_book_primary_key>/', views.approve_borrow_book_request),
    path('for-pickup/read/', views.read_books_for_pick_up),
    path('for-pickup/approve/<int:borrow_book_primary_key>/', views.approve_book_pick_up),
    path('for-return/read/', views.read_books_for_return),
    path('for-return/return/<int:borrow_book_primary_key>/', views.return_book),
]