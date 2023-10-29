from django.urls import path
from . import views

app_name = 'borrow_book'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:primary_key>', views.add, name='add'),
    path('borrow-request/', views.borrow_request, name='borrow_request'),
    path('borrow-request-approve/<int:primary_key>/', views.borrow_request_approve, name='borrow_request_approve'),
    path('book-pick-up/', views.book_pick_up, name='book_pick_up'),
    path('book-pick-up-approve/<int:primary_key>/', views.book_pick_up_approve, name='book_pick_up_approve'),
    path('book-return/', views.book_return, name='book_return'),
    path('book-return-approved/<int:primary_key>/', views.book_return_approved, name='book_return_approved'),
]